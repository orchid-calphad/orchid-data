# Hg–Pb phases

> Hg–Pb system: 6 phases (tier A 4, liquid 1, needs_review 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HG-PB.html · Markdown: https://data.orchid-project.org/phases/pages/HG-PB.md

6 phases (tier A 4, liquid 1, needs_review 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HG-PB) · [full JSON](https://data.orchid-project.org/phases/systems/HG-PB.json) · [Hg–Pb system page](https://data.orchid-project.org/systems/HG-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/HG-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hg–Pb system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBO_A10](#phase-hg-pb-a10-rhombo); _phase:hg-pb:a10-rhombo_ | alpha-Hg · A10 · hR1 · R-3m (166) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCC_A2](#phase-hg-pb-bcc-a2); _phase:hg-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-hg-pb-fcc-a1); _phase:hg-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.25 K, x(Pb) 0.69489–1 | 7 | 1 |
| [HCP_A3](#phase-hg-pb-hcp-a3); _phase:hg-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HGPB2_L10](#phase-hg-pb-hgpb2-l10); _phase:hg-pb:hgpb2-l10_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–429.07 K, x(Pb) 0.66667–0.66667 | 0 | 1 |
| [LIQUID](#phase-hg-pb-liquid); _phase:hg-pb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Pb) 0–1 | 20 | 1 |

## RHOMBO_A10 (Hg–Pb)

- Id: `phase:hg-pb:a10-rhombo`; status `assigned`
- Structure: alpha-Hg · A10 · hR1 · R-3m (166); type `st:a10-alpha-hg-hr1`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-pb:a10-rhombo)

Names (2): _corpus: _corpus:phase:hg-pb:a10-rhombo  
_tdb: _tdb:HgPb-02Mai-LB.tdb:RHOMBO_A10  


### TDB models of RHOMBO_A10 (1): PHASE and CONSTITUENT statements as written

[HgPb-02Mai-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgPb-02Mai-LB.tdb): RHOMBO_A10, type code %, sha256 `7e9650b9546b0f1f…`

~~~~text
55: PHASE RHOMBO_A10 % 1 1 !
56: CONST RHOMBO_A10 : HG PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002).  
_assessment that models this phase_

## BCC_A2 (Hg–Pb)

- Id: `phase:hg-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-pb:bcc-a2)

Names (2): _corpus: _corpus:phase:hg-pb:bcc-a2  
_tdb: _tdb:HgPb-02Mai-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[HgPb-02Mai-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgPb-02Mai-LB.tdb): BCC_A2, type code %B, sha256 `7e9650b9546b0f1f…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002).  
_assessment that models this phase_

## FCC_A1 (Hg–Pb)

- Id: `phase:hg-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.25 K, x(Pb) 0.69489–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-pb:fcc-a1)

Names (4): _corpus: _corpus:phase:hg-pb:fcc-a1  
_paper: _paper:10.1361/105497102770331578:Fcc(Pb), paper:10.1361/105497102770331578:fcc(Pb)  
_tdb: _tdb:HgPb-02Mai-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HgPb-02Mai-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgPb-02Mai-LB.tdb): FCC_A1, type code %A, sha256 `7e9650b9546b0f1f…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : HG PB% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Hg–Pb)

- Id: `phase:hg-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-pb:hcp-a3)

Names (2): _corpus: _corpus:phase:hg-pb:hcp-a3  
_tdb: _tdb:HgPb-02Mai-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HgPb-02Mai-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgPb-02Mai-LB.tdb): HCP_A3, type code %A, sha256 `7e9650b9546b0f1f…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : HG PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002).  
_assessment that models this phase_

## HGPB2_L10 (Hg–Pb)

- Id: `phase:hg-pb:hgpb2-l10`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_L1_0; stoichiometry_contradicts_L1_0:HgPb-02Mai-LB.tdb
- Candidate (name_token): AuCu · L1_0 · tP4 · P4/mmm (123) — Strukturbericht/word 'L10' in the TDB name
- Candidate (sgte_mmc2): AuCu · L1_0 · tP4 · P4/mmm (123) — Hallstedt 2025 mmc2 row for HGPB2_L10: HgPb2
- Candidate (tdb_comment): AuCu · tP4 · P4/mmm — HgPb-02Mai-LB.tdb: 'Prototype AuCu (tP4, P4/mmm)'
- Stoichiometry: Hg 0.3333, Pb 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.07 K, x(Pb) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-pb:hgpb2-l10)

Names (2): _corpus: _corpus:phase:hg-pb:hgpb2-l10  
_tdb: _tdb:HgPb-02Mai-LB.tdb:HGPB2_L10  


### TDB models of HGPB2_L10 (1): PHASE and CONSTITUENT statements as written

[HgPb-02Mai-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgPb-02Mai-LB.tdb): HGPB2_L10, type code %, sha256 `7e9650b9546b0f1f…`

~~~~text
60: PHASE HGPB2_L10 % 2 1 2 !
61: CONST HGPB2_L10 : HG : PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002).  
_assessment that models this phase_

## LIQUID (Hg–Pb)

- Id: `phase:hg-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Pb) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-pb:liquid)

Names (6): _corpus: _corpus:phase:hg-pb:liquid  
_paper: _paper:10.1361/105497102770331578:Liq, paper:10.1361/105497102770331578:Liquid, paper:10.1361/105497102770331578:liq, paper:10.1361/105497102770331578:liquid  
_tdb: _tdb:HgPb-02Mai-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HgPb-02Mai-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgPb-02Mai-LB.tdb): LIQUID, type code %, sha256 `7e9650b9546b0f1f…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : HG PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770331578](https://doi.org/10.1361/105497102770331578) A. Maitre, J. M. Fiorani, M. Vilasi, Thermodynamic study of phase equilibria in the Pb-Bi-Hg system, JPE 23, 329-338 (2002).  
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
