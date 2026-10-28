# Li–O phases

> Li–O system: 9 phases (tier A 4, liquid 2, gas 2, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LI-O.html · Markdown: https://data.orchid-project.org/phases/pages/LI-O.md

9 phases (tier A 4, liquid 2, gas 2, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LI-O) · [full JSON](https://data.orchid-project.org/phases/systems/LI-O.json) · [Li–O system page](https://data.orchid-project.org/systems/LI-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/LI-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Li–O system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-li-o-bcc-a2); _phase:li-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–405 K, x(O) 0–0 | 2 | 1 |
| [FCC_A1](#phase-li-o-fcc-a1); _phase:li-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-li-o-gas); _phase:li-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1611.35–2500 K, x(O) 0–0.99972 | 4 | 1 |
| [HCP_A3](#phase-li-o-hcp-a3); _phase:li-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-li-o-ion); _phase:li-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1611.35–2500 K, x(O) 0–0.33333 | 0 | 1 |
| [LI2O_C1](#phase-li-o-li2o-c1); _phase:li-o:li2o-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–778.65 K, x(O) 0.33333–0.33333 | 13 | 1 |
| [LI2O2](#phase-li-o-li2o2); _phase:li-o:li2o2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–613.65 K, x(O) 0.5–0.5 | 8 | 1 |
| [LIQUID](#phase-li-o-liquid); _phase:li-o:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 6 | 1 |
| [O2GAS](#phase-li-o-o2gas); _phase:li-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–778.65 K, x(O) 1–1 | 0 | 1 |

## BCC_A2 (Li–O)

- Id: `phase:li-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–405 K, x(O) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:bcc-a2)

Names (3): _corpus: _corpus:phase:li-o:bcc-a2  
_paper: _paper:10.1016/j.calphad.2011.02.003:(Li)  
_tdb: _tdb:LiO-11Cha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): BCC_A2, type code %B, sha256 `6943f8b9e741020b…`

~~~~text
51: PHASE BCC_A2 %B 2 1 3 !
52: CONST BCC_A2 : LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667558](https://doi.org/10.1007/bf02667558) J. Sangster, A. D. Pelton, The Li-O (lithium-oxygen) system, JPE 13, 296-299 (1992).  
_cited as the source of values for this phase_

## FCC_A1 (Li–O)

- Id: `phase:li-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:fcc-a1)

Names (2): _corpus: _corpus:phase:li-o:fcc-a1  
_tdb: _tdb:LiO-11Cha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): FCC_A1, type code %A, sha256 `6943f8b9e741020b…`

~~~~text
46: PHASE FCC_A1 %A 2 1 1 !
47: CONST FCC_A1 : LI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
_assessment that models this phase_

## GAS (Li–O)

- Id: `phase:li-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1611.35–2500 K, x(O) 0–0.99972
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:gas)

Names (3): _corpus: _corpus:phase:li-o:gas  
_paper: _paper:10.1016/j.calphad.2011.02.003:Gas  
_tdb: _tdb:LiO-11Cha.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): GAS, type code %, sha256 `6943f8b9e741020b…`

~~~~text
72: PHASE GAS:G % 1 1 !
73: CONST GAS:G : LI LI2 LI2O LI2O2 O O2 O3 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/cr60161a001](https://doi.org/10.1021/cr60161a001) Leo. Brewer, Thermodynamic Properties of the Oxides and their Vaporization Processes., Chem. Rev. 52, 1-75 (1953).  
_cited as the source of values for this phase_

## HCP_A3 (Li–O)

- Id: `phase:li-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:hcp-a3)

Names (2): _corpus: _corpus:phase:li-o:hcp-a3  
_tdb: _tdb:LiO-11Cha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): HCP_A3, type code %A, sha256 `6943f8b9e741020b…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : LI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
_assessment that models this phase_

## ION (Li–O)

- Id: `phase:li-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1611.35–2500 K, x(O) 0–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:ion)

Names (2): _corpus: _corpus:phase:li-o:ion  
_tdb: _tdb:LiO-11Cha.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): ION, type code %, sha256 `6943f8b9e741020b…`

~~~~text
38: PHASE ION:Y % 2 1 1 !
39: CONST ION:Y : LI+1 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
_assessment that models this phase_

## LI2O_C1 (Li–O)

- Id: `phase:li-o:li2o-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–778.65 K, x(O) 0.33333–0.33333
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:li2o-c1)

Names (3): _corpus: _corpus:phase:li-o:li2o-c1  
_paper: _paper:10.1016/j.calphad.2011.02.003:Li2O  
_tdb: _tdb:LiO-11Cha.tdb:LI2O_C1  


### TDB models of LI2O_C1 (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): LI2O_C1, type code %, sha256 `6943f8b9e741020b…`

~~~~text
61: PHASE LI2O_C1 % 2 2 1 !
62: CONST LI2O_C1 : LI+1 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667558](https://doi.org/10.1007/bf02667558) J. Sangster, A. D. Pelton, The Li-O (lithium-oxygen) system, JPE 13, 296-299 (1992).  
_cited as the source of values for this phase_

## LI2O2 (Li–O)

- Id: `phase:li-o:li2o2`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_site_ratios; no_structure_token; off_stoichiometric_model
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP Li2O2 at x(O)=0.5000
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Li1 O1 at x(O)=0.5000
- Candidate (literature_printed): Li2O2 · hP8 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Li2O2 · hP8 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for LI2O2: Li2O2
- Candidate (tdb_comment): Li2O2 · hP8 · P6_3/mmc — LiO-11Cha.tdb: 'Prototype Li2O2 (hP8, P6_3/mmc)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–613.65 K, x(O) 0.5–0.5
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:li2o2)

Names (3): _corpus: _corpus:phase:li-o:li2o2  
_paper: _paper:10.1016/j.calphad.2011.02.003:Li2O2  
_tdb: _tdb:LiO-11Cha.tdb:LI2O2  


### TDB models of LI2O2 (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): LI2O2, type code %, sha256 `6943f8b9e741020b…`

~~~~text
66: PHASE LI2O2 % 2 2 1 !
67: CONST LI2O2 : LI+1 : O2-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Li–O)

- Id: `phase:li-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:liquid)

Names (3): _corpus: _corpus:phase:li-o:liquid  
_paper: _paper:10.1016/j.calphad.2011.02.003:L  
_tdb: _tdb:LiO-11Cha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): LIQUID, type code %, sha256 `6943f8b9e741020b…`

~~~~text
41: PHASE LIQUID:L % 1 1 !
42: CONST LIQUID:L : LI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667558](https://doi.org/10.1007/bf02667558) J. Sangster, A. D. Pelton, The Li-O (lithium-oxygen) system, JPE 13, 296-299 (1992).  
_cited as the source of values for this phase_
- [doi:10.1021/cr60161a001](https://doi.org/10.1021/cr60161a001) Leo. Brewer, Thermodynamic Properties of the Oxides and their Vaporization Processes., Chem. Rev. 52, 1-75 (1953).  
_cited as the source of values for this phase_

## O2GAS (Li–O)

- Id: `phase:li-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–778.65 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-o:o2gas)

Names (2): _corpus: _corpus:phase:li-o:o2gas  
_tdb: _tdb:LiO-11Cha.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[LiO-11Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiO-11Cha.tdb): O2GAS, type code %, sha256 `6943f8b9e741020b…`

~~~~text
69: PHASE O2GAS % 1 1 !
70: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.02.003](https://doi.org/10.1016/j.calphad.2011.02.003) Keke Chang, Bengt Hallstedt, Thermodynamic assessment of the Li–O system, Calphad 35, 160-164 (2011).  
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
