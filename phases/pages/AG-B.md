# Ag–B phases

> Ag–B system: 6 phases (tier A 3, liquid 1, needs_review 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-B.html · Markdown: https://data.orchid-project.org/phases/pages/AG-B.md

6 phases (tier A 3, liquid 1, needs_review 2); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-B) · [full JSON](https://data.orchid-project.org/phases/systems/AG-B.json) · [Ag–B system page](https://data.orchid-project.org/systems/AG-B.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-B.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–B system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ALPHA_RHOMBO_B](#phase-ag-b-b-alpha-rhombo); _phase:ag-b:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-ag-b-b-beta-rhombo); _phase:ag-b:b-beta-rhombo_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–3999.67 K, x(B) 1–1 | 4 | 2 |
| [BCC_A2](#phase-ag-b-bcc-a2); _phase:ag-b:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ag-b-fcc-a1); _phase:ag-b:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1235.48 K, x(B) 0–0.00049 | 2 | 2 |
| [HCP_A3](#phase-ag-b-hcp-a3); _phase:ag-b:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ag-b-liquid); _phase:ag-b:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1234.92–4000 K, x(B) 0–1 | 4 | 2 |

## ALPHA_RHOMBO_B (Ag–B)

- Id: `phase:ag-b:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — AgB-20Zho.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-b:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:ag-b:b-alpha-rhombo  
_tdb: _tdb:AgB-20Zho.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[AgB-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-20Zho.tdb): ALPHA_RHOMBO_B, type code %, sha256 `95c088f2f369a16b…`

~~~~text
45: PHASE ALPHA_RHOMBO_B % 1 1 !
46: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase_

## BETA_RHOMBO_B (Ag–B)

- Id: `phase:ag-b:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — AgB-04Kor-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Candidate (tdb_comment): beta-B · hR105 · R-3m — AgB-20Zho.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.67 K, x(B) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-b:b-beta-rhombo)

Names (5): _corpus: _corpus:phase:ag-b:b-beta-rhombo, corpus:phase:ag-b:beta-rhombo-b  
_paper: _paper:10.1007/s11669-020-00813-5:(βB)  
_tdb: _tdb:AgB-04Kor-LB.tdb:BETA_RHOMBO_B, tdb:AgB-20Zho.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (2): PHASE and CONSTITUENT statements as written

[AgB-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-04Kor-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `433d8df8e0788ba9…`

~~~~text
40: PHASE BETA_RHOMBO_B % 1 1 !
41: CONST BETA_RHOMBO_B : B : !
~~~~

[AgB-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-20Zho.tdb): BETA_RHOMBO_B, type code %, sha256 `95c088f2f369a16b…`

~~~~text
50: PHASE BETA_RHOMBO_B % 1 1 !
51: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Ag–B)

- Id: `phase:ag-b:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-b:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-b:bcc-a2  
_tdb: _tdb:AgB-04Kor-LB.tdb:BCC_A2, tdb:AgB-20Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgB-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-04Kor-LB.tdb): BCC_A2, type code %B, sha256 `433d8df8e0788ba9…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG : B VA% : !
~~~~

[AgB-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-20Zho.tdb): BCC_A2, type code %B, sha256 `95c088f2f369a16b…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : AG B : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase_

## FCC_A1 (Ag–B)

- Id: `phase:ag-b:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1235.48 K, x(B) 0–0.00049
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-b:fcc-a1)

Names (4): _corpus: _corpus:phase:ag-b:fcc-a1  
_paper: _paper:10.1007/s11669-020-00813-5:(Ag)  
_tdb: _tdb:AgB-04Kor-LB.tdb:FCC_A1, tdb:AgB-20Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgB-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-04Kor-LB.tdb): FCC_A1, type code %A, sha256 `433d8df8e0788ba9…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% : B VA% : !
~~~~

[AgB-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-20Zho.tdb): FCC_A1, type code %A, sha256 `95c088f2f369a16b…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : AG% B : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ag–B)

- Id: `phase:ag-b:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-b:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-b:hcp-a3  
_tdb: _tdb:AgB-04Kor-LB.tdb:HCP_A3, tdb:AgB-20Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgB-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-04Kor-LB.tdb): HCP_A3, type code %A, sha256 `433d8df8e0788ba9…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG : B VA% : !
~~~~

[AgB-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-20Zho.tdb): HCP_A3, type code %A, sha256 `95c088f2f369a16b…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : AG B : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
_assessment that models this phase_

## LIQUID (Ag–B)

- Id: `phase:ag-b:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1234.92–4000 K, x(B) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-b:liquid)

Names (4): _corpus: _corpus:phase:ag-b:liquid  
_paper: _paper:10.1007/s11669-020-00813-5:Liquid#1  
_tdb: _tdb:AgB-04Kor-LB.tdb:LIQUID, tdb:AgB-20Zho.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgB-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-04Kor-LB.tdb): LIQUID, type code %, sha256 `433d8df8e0788ba9…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG B : !
~~~~

[AgB-20Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/AgB-20Zho.tdb): LIQUID, type code %, sha256 `95c088f2f369a16b…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : AG B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-020-00813-5](https://doi.org/10.1007/s11669-020-00813-5) Jiaqiang Zhou, Biao Hu, Yu Jiang, Chengliang Qiu, Yong Du, Huiqin Yin, Thermodynamic Modeling of the Ag-X (X = B, Fe, Sm, Pu) Binary Systems, J. Phase Equilib. Diffus. 41, 257-268 (2020).  
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
