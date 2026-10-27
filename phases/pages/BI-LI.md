# Bi–Li phases

> Bi–Li system: 8 phases (tier A 6, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-LI.html · Markdown: https://data.orchid-project.org/phases/pages/BI-LI.md

8 phases (tier A 6, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-LI) · [full JSON](https://data.orchid-project.org/phases/systems/BI-LI.json) · [Bi–Li system page](https://data.orchid-project.org/systems/BI-LI.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-LI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Li system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-li-a7-rhombohedral); _phase:bi-li:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Li) 0–0 | 2 | 1 |
| [BCC_A2](#phase-bi-li-bcc-a2); _phase:bi-li:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–454.6 K, x(Li) 1–1 | 2 | 1 |
| [BILI_HT](#phase-bi-li-bili); _phase:bi-li:bili_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 680–680 K, x(Li) 0.5–0.5 | 3 | 1 |
| [BILI_L10](#phase-bi-li-bili-l10); _phase:bi-li:bili-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–670 K, x(Li) 0.5–0.5 | 5 | 1 |
| [BILI3_D03](#phase-bi-li-bili3-d03); _phase:bi-li:bili3-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1431.82 K, x(Li) 0.75–0.75 | 8 | 1 |
| [FCC_A1](#phase-bi-li-fcc-a1); _phase:bi-li:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-li-hcp-a3); _phase:bi-li:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-bi-li-liquid); _phase:bi-li:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 453.07–2500 K, x(Li) 0–1 | 14 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Li)

- Id: `phase:bi-li:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Li) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-li:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-li:a7-rhombohedral, corpus:phase:bi-li:rhombohedral-a7  
_paper: _paper:10.1016/j.tca.2013.01.029:Bi  
_tdb: _tdb:BiLi-13Liu.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiLi-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `15b3439c7d98d6a9…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Bi–Li)

- Id: `phase:bi-li:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–454.6 K, x(Li) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-li:bcc-a2)

Names (3): _corpus: _corpus:phase:bi-li:bcc-a2  
_paper: _paper:10.1016/j.tca.2013.01.029:Li  
_tdb: _tdb:BiLi-13Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiLi-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb): BCC_A2, type code %B, sha256 `15b3439c7d98d6a9…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI LI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_

## BILI_HT (Bi–Li)

- Id: `phase:bi-li:bili`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition; sgte_mmc2_row_incomplete
- Candidate (dft_mp): P4/mmm (123) — on-hull MP LiBi at x(LI)=0.5000
- Candidate (dft_oqmd): P4/mmm (123) — on-hull OQMD Bi1 Li1 at x(LI)=0.5000
- Candidate (literature_printed): (BiLi) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (BiLi) — Hallstedt 2025 mmc2 row for BILI_HT: BiLi (high T)
- Stoichiometry: Bi 0.5000, Li 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 680–680 K, x(Li) 0.5–0.5
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-li:bili)

Names (4): _corpus: _corpus:phase:bi-li:bili, corpus:phase:bi-li:bili-ht  
_paper: _paper:10.1016/j.tca.2013.01.029:βBiLi  
_tdb: _tdb:BiLi-13Liu.tdb:BILI_HT  


### TDB models of BILI_HT (1): PHASE and CONSTITUENT statements as written

[BiLi-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb): BILI_HT, type code %, sha256 `15b3439c7d98d6a9…`

~~~~text
55: PHASE BILI_HT % 2 1 1 !
56: CONST BILI_HT : BI : LI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2131401](https://doi.org/10.1149/1.2131401) W. Weppner, R. A. Huggins, Thermodynamic Properties of the Intermetallic Systems Lithium‐Antimony and Lithium‐Bismuth, J. Electrochem. Soc. 125, 7-14 (1978).  
_cited as the source of values for this phase_

## BILI_L10 (Bi–Li)

- Id: `phase:bi-li:bili-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, Li 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–670 K, x(Li) 0.5–0.5
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-li:bili-l10)

Names (3): _corpus: _corpus:phase:bi-li:bili-l10  
_paper: _paper:10.1016/j.tca.2013.01.029:αBiLi  
_tdb: _tdb:BiLi-13Liu.tdb:BILI_L10  


### TDB models of BILI_L10 (1): PHASE and CONSTITUENT statements as written

[BiLi-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb): BILI_L10, type code %, sha256 `15b3439c7d98d6a9…`

~~~~text
50: PHASE BILI_L10 % 2 1 1 !
51: CONST BILI_L10 : BI : LI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2131401](https://doi.org/10.1149/1.2131401) W. Weppner, R. A. Huggins, Thermodynamic Properties of the Intermetallic Systems Lithium‐Antimony and Lithium‐Bismuth, J. Electrochem. Soc. 125, 7-14 (1978).  
_cited as the source of values for this phase_

## BILI3_D03 (Bi–Li)

- Id: `phase:bi-li:bili3-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabije and oqmd-10938, space group 225
- Stoichiometry: Bi 0.2500, Li 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1431.82 K, x(Li) 0.75–0.75
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-li:bili3-d03)

Names (5): _corpus: _corpus:phase:bi-li:bili3-d03  
_mp: _mp:mp-aaaabije  
_oqmd: _oqmd:oqmd-10938  
_paper: _paper:10.1016/j.tca.2013.01.029:BiLi3  
_tdb: _tdb:BiLi-13Liu.tdb:BILI3_D03  


### TDB models of BILI3_D03 (1): PHASE and CONSTITUENT statements as written

[BiLi-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb): BILI3_D03, type code %, sha256 `15b3439c7d98d6a9…`

~~~~text
60: PHASE BILI3_D03 % 2 1 3 !
61: CONST BILI3_D03 : BI : LI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2131401](https://doi.org/10.1149/1.2131401) W. Weppner, R. A. Huggins, Thermodynamic Properties of the Intermetallic Systems Lithium‐Antimony and Lithium‐Bismuth, J. Electrochem. Soc. 125, 7-14 (1978).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Li)

- Id: `phase:bi-li:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-li:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-li:fcc-a1  
_tdb: _tdb:BiLi-13Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiLi-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb): FCC_A1, type code %A, sha256 `15b3439c7d98d6a9…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI LI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase_

## HCP_A3 (Bi–Li)

- Id: `phase:bi-li:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-li:hcp-a3)

Names (2): _corpus: _corpus:phase:bi-li:hcp-a3  
_tdb: _tdb:BiLi-13Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiLi-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb): HCP_A3, type code %A, sha256 `15b3439c7d98d6a9…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI LI : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase_

## LIQUID (Bi–Li)

- Id: `phase:bi-li:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 453.07–2500 K, x(Li) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-li:liquid)

Names (4): _corpus: _corpus:phase:bi-li:liquid  
_paper: _paper:10.1016/j.tca.2013.01.029:liq, paper:10.1016/j.tca.2013.01.029:liquid  
_tdb: _tdb:BiLi-13Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiLi-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiLi-13Liu.tdb): LIQUID, type code %, sha256 `15b3439c7d98d6a9…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI BILI3 LI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1149/1.2131401](https://doi.org/10.1149/1.2131401) W. Weppner, R. A. Huggins, Thermodynamic Properties of the Intermetallic Systems Lithium‐Antimony and Lithium‐Bismuth, J. Electrochem. Soc. 125, 7-14 (1978).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645966](https://doi.org/10.1007/bf02645966) J. Sangster, A.D. Pelton, The Bi–Li (bismuth–lithium) system, J. Phase Equilib. 12 (1991) 447–450.  
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
