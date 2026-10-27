# Mo–Ru phases

> Mo–Ru system: 7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-RU.html · Markdown: https://data.orchid-project.org/phases/pages/MO-RU.md

7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-RU) · [full JSON](https://data.orchid-project.org/phases/systems/MO-RU.json) · [Mo–Ru system page](https://data.orchid-project.org/systems/MO-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Ru system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [SIGMA_ALT](#phase-mo-ru-alt-sigma); _phase:mo-ru:alt-sigma_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1415.99–2180 K, x(Ru) 0.37–0.38 | 0 | 1 |
| [BCC_A2](#phase-mo-ru-bcc-a2); _phase:mo-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2907.01 K, x(Ru) 0–0.32265 | 9 | 3 |
| [SIGMA_D8B](#phase-mo-ru-d8b-sigma); _phase:mo-ru:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1414.24–2189.52 K, x(Ru) 0.37303–0.39078 | 0 | 2 |
| [FCC_A1](#phase-mo-ru-fcc-a1); _phase:mo-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-mo-ru-hcp-a3); _phase:mo-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2607 K, x(Ru) 0.48792–1 | 9 | 3 |
| [LIQUID](#phase-mo-ru-liquid); _phase:mo-ru:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 2227.98–4000 K, x(Ru) 0–1 | 3 | 3 |
| [SIGMA_OLD](#phase-mo-ru-old-sigma); _phase:mo-ru:old-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1414.45–2189.54 K, x(Ru) 0.36817–0.38292 | 6 | 1 |

## SIGMA_ALT (Mo–Ru)

- Id: `phase:mo-ru:alt-sigma`; status `needs_review`
- No structure assigned. Why: unrecognised_name_tokens:ALT
- Candidate (name_token): sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) — Strukturbericht/word 'D8B' in the TDB name
- Candidate (tdb_comment): CrFe · tP30 · P4_2/mnm — MoRu-21Liu.tdb: 'Prototype CrFe (tP30, P4_2/mnm), alternative sigma model'
- Stability: stable in 1 of 1 calculated diagram(s): 1415.99–2180 K, x(Ru) 0.37–0.38
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ru:alt-sigma)

Names (2): _corpus: _corpus:phase:mo-ru:alt-sigma  
_tdb: _tdb:MoRu-21Liu.tdb:SIGMA_ALT  


### TDB models of SIGMA_ALT (1): PHASE and CONSTITUENT statements as written

[MoRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-21Liu.tdb): SIGMA_ALT, type code %, sha256 `ca6f85caeed3576c…`

~~~~text
49: PHASE SIGMA_ALT % 2 10 20 !
50: CONST SIGMA_ALT : MO RU : MO RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_

## BCC_A2 (Mo–Ru)

- Id: `phase:mo-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2907.01 K, x(Ru) 0–0.32265
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ru:bcc-a2)

Names (5): _corpus: _corpus:phase:mo-ru:bcc-a2  
_paper: _paper:10.1016/s0925-8388(00)01192-0:bcc  
_tdb: _tdb:MoRu-00Oh-oldsigma.tdb:BCC_A2, tdb:MoRu-00Oh.tdb:BCC_A2, tdb:MoRu-21Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MoRu-00Oh-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh-oldsigma.tdb): BCC_A2, type code %B, sha256 `90b4291aface7903…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MO% RU : VA : !
~~~~

[MoRu-00Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh.tdb): BCC_A2, type code %B, sha256 `7638f7116eda1f73…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MO% RU : VA : !
~~~~

[MoRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-21Liu.tdb): BCC_A2, type code %B, sha256 `ca6f85caeed3576c…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MO% RU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(00)01192-0](https://doi.org/10.1016/S0925-8388%2800%2901192-0) C.-S. Oh, H. Murakami, H. Harada, J. Alloys Compd., 313, 115-20(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_

## SIGMA_D8B (Mo–Ru)

- Id: `phase:mo-ru:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoRu-21Liu.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 1414.24–2189.52 K, x(Ru) 0.37303–0.39078
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ru:d8b-sigma)

Names (3): _corpus: _corpus:phase:mo-ru:d8b-sigma  
_tdb: _tdb:MoRu-00Oh.tdb:SIGMA_D8B, tdb:MoRu-21Liu.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (2): PHASE and CONSTITUENT statements as written

[MoRu-00Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh.tdb): SIGMA_D8B, type code %, sha256 `7638f7116eda1f73…`

~~~~text
44: PHASE SIGMA_D8B % 3 10 4 16 !
45: CONST SIGMA_D8B : RU : MO : MO RU : !
~~~~

[MoRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-21Liu.tdb): SIGMA_D8B, type code %, sha256 `ca6f85caeed3576c…`

~~~~text
44: PHASE SIGMA_D8B % 3 10 4 16 !
45: CONST SIGMA_D8B : MO RU : MO RU : MO RU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01192-0](https://doi.org/10.1016/S0925-8388%2800%2901192-0) C.-S. Oh, H. Murakami, H. Harada, J. Alloys Compd., 313, 115-20(2000).  
_assessment that models this phase_

## FCC_A1 (Mo–Ru)

- Id: `phase:mo-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ru:fcc-a1)

Names (4): _corpus: _corpus:phase:mo-ru:fcc-a1  
_tdb: _tdb:MoRu-00Oh-oldsigma.tdb:FCC_A1, tdb:MoRu-00Oh.tdb:FCC_A1, tdb:MoRu-21Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MoRu-00Oh-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh-oldsigma.tdb): FCC_A1, type code %A, sha256 `90b4291aface7903…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MO RU : VA : !
~~~~

[MoRu-00Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh.tdb): FCC_A1, type code %A, sha256 `7638f7116eda1f73…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MO RU : VA : !
~~~~

[MoRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-21Liu.tdb): FCC_A1, type code %A, sha256 `ca6f85caeed3576c…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MO RU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(00)01192-0](https://doi.org/10.1016/S0925-8388%2800%2901192-0) C.-S. Oh, H. Murakami, H. Harada, J. Alloys Compd., 313, 115-20(2000).  
_assessment that models this phase_

## HCP_A3 (Mo–Ru)

- Id: `phase:mo-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2607 K, x(Ru) 0.48792–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ru:hcp-a3)

Names (5): _corpus: _corpus:phase:mo-ru:hcp-a3  
_paper: _paper:10.1016/s0925-8388(00)01192-0:hcp  
_tdb: _tdb:MoRu-00Oh-oldsigma.tdb:HCP_A3, tdb:MoRu-00Oh.tdb:HCP_A3, tdb:MoRu-21Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MoRu-00Oh-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh-oldsigma.tdb): HCP_A3, type code %A, sha256 `90b4291aface7903…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MO RU% : VA : !
~~~~

[MoRu-00Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh.tdb): HCP_A3, type code %A, sha256 `7638f7116eda1f73…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MO RU% : VA : !
~~~~

[MoRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-21Liu.tdb): HCP_A3, type code %A, sha256 `ca6f85caeed3576c…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MO RU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(00)01192-0](https://doi.org/10.1016/S0925-8388%2800%2901192-0) C.-S. Oh, H. Murakami, H. Harada, J. Alloys Compd., 313, 115-20(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_

## LIQUID (Mo–Ru)

- Id: `phase:mo-ru:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2227.98–4000 K, x(Ru) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ru:liquid)

Names (5): _corpus: _corpus:phase:mo-ru:liquid  
_paper: _paper:10.1016/s0925-8388(00)01192-0:L  
_tdb: _tdb:MoRu-00Oh-oldsigma.tdb:LIQUID, tdb:MoRu-00Oh.tdb:LIQUID, tdb:MoRu-21Liu.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MoRu-00Oh-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh-oldsigma.tdb): LIQUID, type code %, sha256 `90b4291aface7903…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MO RU : !
~~~~

[MoRu-00Oh.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh.tdb): LIQUID, type code %, sha256 `7638f7116eda1f73…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MO RU : !
~~~~

[MoRu-21Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-21Liu.tdb): LIQUID, type code %, sha256 `ca6f85caeed3576c…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MO RU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(00)01192-0](https://doi.org/10.1016/S0925-8388%2800%2901192-0) C.-S. Oh, H. Murakami, H. Harada, J. Alloys Compd., 313, 115-20(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.102239](https://doi.org/10.1016/j.calphad.2020.102239) J. Liu, C. Zhou, H. Wang, Calphad, 72, 102239(2021).  
_assessment that models this phase_

## SIGMA_OLD (Mo–Ru)

- Id: `phase:mo-ru:old-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1414.45–2189.54 K, x(Ru) 0.36817–0.38292
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-ru:old-sigma)

Names (4): _corpus: _corpus:phase:mo-ru:old-sigma, corpus:phase:mo-ru:sigma-old  
_paper: _paper:10.1016/s0925-8388(00)01192-0:σ  
_tdb: _tdb:MoRu-00Oh-oldsigma.tdb:SIGMA_OLD  


### TDB models of SIGMA_OLD (1): PHASE and CONSTITUENT statements as written

[MoRu-00Oh-oldsigma.tdb](https://orchid-project.org/data/databases/sgte-binary/MoRu-00Oh-oldsigma.tdb): SIGMA_OLD, type code %, sha256 `90b4291aface7903…`

~~~~text
45: PHASE SIGMA_OLD % 3 8 4 18 !
46: CONST SIGMA_OLD : RU : MO : MO RU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(00)01192-0](https://doi.org/10.1016/S0925-8388%2800%2901192-0) C.-S. Oh, H. Murakami, H. Harada, J. Alloys Compd., 313, 115-20(2000).  
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
