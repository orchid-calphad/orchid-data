# Au–Te phases

> Au–Te system: 6 phases (tier A 4, liquid 1, needs_review 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-TE.html · Markdown: https://data.orchid-project.org/phases/pages/AU-TE.md

6 phases (tier A 4, liquid 1, needs_review 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-TE) · [full JSON](https://data.orchid-project.org/phases/systems/AU-TE.json) · [Au–Te system page](https://data.orchid-project.org/systems/AU-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Te system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-au-te-a8-hexagonal); _phase:au-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 5 | 2 |
| [AUTE2_C34](#phase-au-te-aute2-c34); _phase:au-te:aute2-c34_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–738.45 K, x(Te) 0.66667–0.66667 | 14 | 2 |
| [BCC_A2](#phase-au-te-bcc-a2); _phase:au-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-au-te-fcc-a1); _phase:au-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1350.93 K, x(Te) 0–0 | 5 | 2 |
| [HCP_A3](#phase-au-te-hcp-a3); _phase:au-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-au-te-liquid); _phase:au-te:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 688.82–2500 K, x(Te) 0–1 | 14 | 2 |

## HEXAGONAL_A8 (Au–Te)

- Id: `phase:au-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:au-te:a8-hexagonal  
_paper: _paper:10.1016/j.jallcom.2005.05.038:hex (Te)  
_tdb: _tdb:AuTe-06Wan.tdb:HEXAGONAL_A8, tdb:AuTe-94Feu-LB.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[AuTe-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-06Wan.tdb): HEXAGONAL_A8, type code %, sha256 `03172f4e43a2f653…`

~~~~text
47: PHASE HEXAGONAL_A8 % 1 1 !
48: CONST HEXAGONAL_A8 : TE : !
~~~~

[AuTe-94Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-94Feu-LB.tdb): HEXAGONAL_A8, type code %, sha256 `92fa89b9beed51a9…`

~~~~text
56: PHASE HEXAGONAL_A8 % 1 1 !
57: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.05.038](https://doi.org/10.1016/j.jallcom.2005.05.038) Jianhua Wang, Xiao-gang Lu, Bo Sundman, Xuping Su, Thermodynamic reassessment of the Au–Te system, Journal of Alloys and Compounds 407, 106-111 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02647557](https://doi.org/10.1007/BF02647557) Y. Feutelais, D. Mouani, J.R. Didry, B. Legendre, J. Phase Equilib., 15, 380-85(1994).  
_assessment that models this phase_
- [doi:10.1002/bbpc.19770811024](https://doi.org/10.1002/bbpc.19770811024) C. Bergman, R. Castanet, Thermodynamic Investigation on the Au — Te Binary System, Ber Bunsenges Phys Chem 81, 1000-1003 (1977).  
_cited as the source of values for this phase_

## AUTE2_C34 (Au–Te)

- Id: `phase:au-te:aute2-c34`; status `needs_review`
- No structure assigned. Why: name_suggests_C34_but_dft_space_group_28
- Candidate (dft_mp): Pma2 (28) — on-hull MP Te2Au at x(TE)=0.6667
- Candidate (dft_oqmd): Pma2 (28) — on-hull OQMD Au1 Te2 at x(TE)=0.6667
- Candidate (name_token): AuTe2 · C34 · mC6 · C2/m (12) — Strukturbericht/word 'C34' in the TDB name
- Candidate (tdb_comment): AuTe2 · mC6 · C2/m — AuTe-06Wan.tdb: 'Prototype AuTe2 (mC6, C2/m)'
- Candidate (tdb_comment): AuTe2 · mC6 · C2/m — AuTe-94Feu-LB.tdb: 'Prototype AuTe2 (mC6, C2/m)'
- Stoichiometry: Au 0.3333, Te 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–738.45 K, x(Te) 0.66667–0.66667
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-te:aute2-c34)

Names (4): _corpus: _corpus:phase:au-te:aute2-c34  
_paper: _paper:10.1016/j.jallcom.2005.05.038:AuTe2  
_tdb: _tdb:AuTe-06Wan.tdb:AUTE2_C34, tdb:AuTe-94Feu-LB.tdb:AUTE2_C34  


### TDB models of AUTE2_C34 (2): PHASE and CONSTITUENT statements as written

[AuTe-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-06Wan.tdb): AUTE2_C34, type code %, sha256 `03172f4e43a2f653…`

~~~~text
52: PHASE AUTE2_C34 % 2 1 2 !
53: CONST AUTE2_C34 : AU : TE : !
~~~~

[AuTe-94Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-94Feu-LB.tdb): AUTE2_C34, type code %, sha256 `92fa89b9beed51a9…`

~~~~text
61: PHASE AUTE2_C34 % 2 1 2 !
62: CONST AUTE2_C34 : AU : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.05.038](https://doi.org/10.1016/j.jallcom.2005.05.038) Jianhua Wang, Xiao-gang Lu, Bo Sundman, Xuping Su, Thermodynamic reassessment of the Au–Te system, Journal of Alloys and Compounds 407, 106-111 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02647557](https://doi.org/10.1007/BF02647557) Y. Feutelais, D. Mouani, J.R. Didry, B. Legendre, J. Phase Equilib., 15, 380-85(1994).  
_assessment that models this phase_
- [doi:10.1002/bbpc.19770811024](https://doi.org/10.1002/bbpc.19770811024) C. Bergman, R. Castanet, Thermodynamic Investigation on the Au — Te Binary System, Ber Bunsenges Phys Chem 81, 1000-1003 (1977).  
_cited as the source of values for this phase_

## BCC_A2 (Au–Te)

- Id: `phase:au-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-te:bcc-a2)

Names (3): _corpus: _corpus:phase:au-te:bcc-a2  
_tdb: _tdb:AuTe-06Wan.tdb:BCC_A2, tdb:AuTe-94Feu-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AuTe-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-06Wan.tdb): BCC_A2, type code %B, sha256 `03172f4e43a2f653…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AU : VA : !
~~~~

[AuTe-94Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-94Feu-LB.tdb): BCC_A2, type code %B, sha256 `92fa89b9beed51a9…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : AU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647557](https://doi.org/10.1007/BF02647557) Y. Feutelais, D. Mouani, J.R. Didry, B. Legendre, J. Phase Equilib., 15, 380-85(1994).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.05.038](https://doi.org/10.1016/j.jallcom.2005.05.038) Jianhua Wang, Xiao-gang Lu, Bo Sundman, Xuping Su, Thermodynamic reassessment of the Au–Te system, Journal of Alloys and Compounds 407, 106-111 (2006).  
_assessment that models this phase_

## FCC_A1 (Au–Te)

- Id: `phase:au-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1350.93 K, x(Te) 0–0
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-te:fcc-a1)

Names (4): _corpus: _corpus:phase:au-te:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2005.05.038:fcc (Au)  
_tdb: _tdb:AuTe-06Wan.tdb:FCC_A1, tdb:AuTe-94Feu-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AuTe-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-06Wan.tdb): FCC_A1, type code %A, sha256 `03172f4e43a2f653…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AU : VA : !
~~~~

[AuTe-94Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-94Feu-LB.tdb): FCC_A1, type code %A, sha256 `92fa89b9beed51a9…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : AU : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.05.038](https://doi.org/10.1016/j.jallcom.2005.05.038) Jianhua Wang, Xiao-gang Lu, Bo Sundman, Xuping Su, Thermodynamic reassessment of the Au–Te system, Journal of Alloys and Compounds 407, 106-111 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02647557](https://doi.org/10.1007/BF02647557) Y. Feutelais, D. Mouani, J.R. Didry, B. Legendre, J. Phase Equilib., 15, 380-85(1994).  
_assessment that models this phase_
- [doi:10.1002/bbpc.19770811024](https://doi.org/10.1002/bbpc.19770811024) C. Bergman, R. Castanet, Thermodynamic Investigation on the Au — Te Binary System, Ber Bunsenges Phys Chem 81, 1000-1003 (1977).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Te)

- Id: `phase:au-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-te:hcp-a3)

Names (3): _corpus: _corpus:phase:au-te:hcp-a3  
_tdb: _tdb:AuTe-06Wan.tdb:HCP_A3, tdb:AuTe-94Feu-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AuTe-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-06Wan.tdb): HCP_A3, type code %A, sha256 `03172f4e43a2f653…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AU : VA : !
~~~~

[AuTe-94Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-94Feu-LB.tdb): HCP_A3, type code %A, sha256 `92fa89b9beed51a9…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : AU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02647557](https://doi.org/10.1007/BF02647557) Y. Feutelais, D. Mouani, J.R. Didry, B. Legendre, J. Phase Equilib., 15, 380-85(1994).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2005.05.038](https://doi.org/10.1016/j.jallcom.2005.05.038) Jianhua Wang, Xiao-gang Lu, Bo Sundman, Xuping Su, Thermodynamic reassessment of the Au–Te system, Journal of Alloys and Compounds 407, 106-111 (2006).  
_assessment that models this phase_

## LIQUID (Au–Te)

- Id: `phase:au-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 688.82–2500 K, x(Te) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-te:liquid)

Names (4): _corpus: _corpus:phase:au-te:liquid  
_paper: _paper:10.1016/j.jallcom.2005.05.038:L  
_tdb: _tdb:AuTe-06Wan.tdb:LIQUID, tdb:AuTe-94Feu-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AuTe-06Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-06Wan.tdb): LIQUID, type code %, sha256 `03172f4e43a2f653…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AU TE : !
~~~~

[AuTe-94Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuTe-94Feu-LB.tdb): LIQUID, type code %, sha256 `92fa89b9beed51a9…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : AU TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2005.05.038](https://doi.org/10.1016/j.jallcom.2005.05.038) Jianhua Wang, Xiao-gang Lu, Bo Sundman, Xuping Su, Thermodynamic reassessment of the Au–Te system, Journal of Alloys and Compounds 407, 106-111 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02647557](https://doi.org/10.1007/BF02647557) Y. Feutelais, D. Mouani, J.R. Didry, B. Legendre, J. Phase Equilib., 15, 380-85(1994).  
_assessment that models this phase_
- [doi:10.1002/bbpc.19770811024](https://doi.org/10.1002/bbpc.19770811024) C. Bergman, R. Castanet, Thermodynamic Investigation on the Au — Te Binary System, Ber Bunsenges Phys Chem 81, 1000-1003 (1977).  
_cited as the source of values for this phase_

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
