# Cd–Cu phases

> Cd–Cu system: 8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-CU.html · Markdown: https://data.orchid-project.org/phases/pages/CD-CU.md

8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-CU) · [full JSON](https://data.orchid-project.org/phases/systems/CD-CU.json) · [Cd–Cu system page](https://data.orchid-project.org/systems/CD-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Cu system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-cu-bcc-a2); _phase:cd-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CD10CU3_D811](#phase-cd-cu-cd10cu3-d811); _phase:cd-cu:cd10cu3-d811_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–673.11 K, x(Cu) 0.23077–0.23077 | 4 | 1 |
| [CD3CU4](#phase-cd-cu-cd3cu4); _phase:cd-cu:cd3cu4_ | Cd3Cu4 · cF1124 · F-43m (216) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–821.06 K, x(Cu) 0.57143–0.57143 | 4 | 1 |
| [CD8CU5_D82](#phase-cd-cu-cd8cu5-d82); _phase:cd-cu:cd8cu5-d82_ | Cu5Zn8 · D8_2 · cI52 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–839.11 K, x(Cu) 0.34166–0.47959 | 6 | 1 |
| [CDCU2_C14](#phase-cd-cu-cdcu2-c14); _phase:cd-cu:cdcu2-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–822.48 K, x(Cu) 0.66667–0.66667 | 4 | 1 |
| [FCC_A1](#phase-cd-cu-fcc-a1); _phase:cd-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.98 K, x(Cu) 0.97523–1 | 2 | 1 |
| [HCP_A3](#phase-cd-cu-hcp-a3); _phase:cd-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–594.22 K, x(Cu) 0–0.00115 | 2 | 1 |
| [LIQUID](#phase-cd-cu-liquid); _phase:cd-cu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 590.72–2500 K, x(Cu) 0–1 | 12 | 1 |

## BCC_A2 (Cd–Cu)

- Id: `phase:cd-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-cu:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-cu:bcc-a2  
_tdb: _tdb:CdCu-10Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdCu-10Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb): BCC_A2, type code %B, sha256 `80095fae64d3c1aa…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CD CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010).  
_assessment that models this phase_

## CD10CU3_D811 (Cd–Cu)

- Id: `phase:cd-cu:cd10cu3-d811`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D8_11; stoichiometry_contradicts_D8_11:CdCu-10Che.tdb
- Candidate (literature_printed): Al5Co2 · hP28 — printed with a label mapped to this phase
- Candidate (name_token): Al5Co2 · D8_11 · hP28 · P6_3/mmc (194) — Strukturbericht/word 'D811' in the TDB name
- Candidate (sgte_mmc2): Al5Co2 · D8_11 · hP28 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for CD10CU3_D811: Cd10Cu3
- Candidate (tdb_comment): Al5Co2 · hP28 · P6_3/mmc — CdCu-10Che.tdb: 'Prototype Al5Co2 (hP28, P6_3/mmc)'
- Stoichiometry: Cd 0.7692, Cu 0.2308
- Stability: stable in 1 of 1 calculated diagram(s): 300–673.11 K, x(Cu) 0.23077–0.23077
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-cu:cd10cu3-d811)

Names (3): _corpus: _corpus:phase:cd-cu:cd10cu3-d811  
_paper: _paper:10.1016/s1003-6326(09)60193-x:Cu3Cd10  
_tdb: _tdb:CdCu-10Che.tdb:CD10CU3_D811  


### TDB models of CD10CU3_D811 (1): PHASE and CONSTITUENT statements as written

[CdCu-10Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb): CD10CU3_D811, type code %, sha256 `80095fae64d3c1aa…`

~~~~text
43: PHASE CD10CU3_D811 % 2 10 3 !
44: CONST CD10CU3_D811 : CD : CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010).  
_assessment that models this phase; reports values for this phase_

## CD3CU4 (Cd–Cu)

- Id: `phase:cd-cu:cd3cu4`; status `assigned`
- Structure: Cd3Cu4 · cF1124 · F-43m (216); type `st:cd3cu4-cf1124`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.4286, Cu 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–821.06 K, x(Cu) 0.57143–0.57143
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-cu:cd3cu4)

Names (3): _corpus: _corpus:phase:cd-cu:cd3cu4  
_paper: _paper:10.1016/s1003-6326(09)60193-x:Cu4Cd3  
_tdb: _tdb:CdCu-10Che.tdb:CD3CU4  


### TDB models of CD3CU4 (1): PHASE and CONSTITUENT statements as written

[CdCu-10Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb): CD3CU4, type code %, sha256 `80095fae64d3c1aa…`

~~~~text
53: PHASE CD3CU4 % 2 3 4 !
54: CONST CD3CU4 : CD : CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010).  
_assessment that models this phase; reports values for this phase_

## CD8CU5_D82 (Cd–Cu)

- Id: `phase:cd-cu:cd8cu5-d82`; status `assigned`
- Structure: Cu5Zn8 · D8_2 · cI52 · I-43m (217); type `st:d8-2-cu5zn8-ci52`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CdCu-10Che.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–839.11 K, x(Cu) 0.34166–0.47959
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-cu:cd8cu5-d82)

Names (3): _corpus: _corpus:phase:cd-cu:cd8cu5-d82  
_paper: _paper:10.1016/s1003-6326(09)60193-x:Cu5Cd8  
_tdb: _tdb:CdCu-10Che.tdb:CD8CU5_D82  


### TDB models of CD8CU5_D82 (1): PHASE and CONSTITUENT statements as written

[CdCu-10Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb): CD8CU5_D82, type code %, sha256 `80095fae64d3c1aa…`

~~~~text
48: PHASE CD8CU5_D82 % 2 8 5 !
49: CONST CD8CU5_D82 : CD% CU : CD CU% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010).  
_assessment that models this phase; reports values for this phase_

## CDCU2_C14 (Cd–Cu)

- Id: `phase:cd-cu:cdcu2-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.3333, Cu 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–822.48 K, x(Cu) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-cu:cdcu2-c14)

Names (3): _corpus: _corpus:phase:cd-cu:cdcu2-c14  
_paper: _paper:10.1016/s1003-6326(09)60193-x:Cu2Cd  
_tdb: _tdb:CdCu-10Che.tdb:CDCU2_C14  


### TDB models of CDCU2_C14 (1): PHASE and CONSTITUENT statements as written

[CdCu-10Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb): CDCU2_C14, type code %, sha256 `80095fae64d3c1aa…`

~~~~text
58: PHASE CDCU2_C14 % 2 1 2 !
59: CONST CDCU2_C14 : CD : CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Cd–Cu)

- Id: `phase:cd-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.98 K, x(Cu) 0.97523–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-cu:fcc-a1)

Names (3): _corpus: _corpus:phase:cd-cu:fcc-a1  
_paper: _paper:10.1016/s1003-6326(09)60193-x:(Cu)  
_tdb: _tdb:CdCu-10Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdCu-10Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb): FCC_A1, type code %A, sha256 `80095fae64d3c1aa…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CD CU% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Cd–Cu)

- Id: `phase:cd-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–594.22 K, x(Cu) 0–0.00115
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-cu:hcp-a3)

Names (3): _corpus: _corpus:phase:cd-cu:hcp-a3  
_paper: _paper:10.1016/s1003-6326(09)60193-x:(Cd)  
_tdb: _tdb:CdCu-10Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdCu-10Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb): HCP_A3, type code %A, sha256 `80095fae64d3c1aa…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CD% CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Cd–Cu)

- Id: `phase:cd-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 590.72–2500 K, x(Cu) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-cu:liquid)

Names (3): _corpus: _corpus:phase:cd-cu:liquid  
_paper: _paper:10.1016/s1003-6326(09)60193-x:L  
_tdb: _tdb:CdCu-10Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdCu-10Che.tdb](https://orchid-project.org/data/databases/sgte-binary/CdCu-10Che.tdb): LIQUID, type code %, sha256 `80095fae64d3c1aa…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CD CU : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S1003-6326(09)60193-X](https://doi.org/10.1016/S1003-6326%2809%2960193-X) X.M. Chen, L.B. Liu, L.G. Zhang, H. Bo, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 20, 649-54(2010).  
_assessment that models this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
