# Er–Mg phases

> Er–Mg system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ER-MG.html · Markdown: https://data.orchid-project.org/phases/pages/ER-MG.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ER-MG) · [full JSON](https://data.orchid-project.org/phases/systems/ER-MG.json) · [Er–Mg system page](https://data.orchid-project.org/systems/ER-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/ER-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Er–Mg system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-er-mg-bcc-a2); _phase:er-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 944.85–1530 K, x(Mg) 0.14533–0.43804 | 0 | 2 |
| [B2_BCC](#phase-er-mg-bcc-b2); _phase:er-mg:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1530 K, x(Mg) 0.14533–0.62073 | 0 | 1 |
| [C14_LAVES](#phase-er-mg-c14-laves); _phase:er-mg:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–952.28 K, x(Mg) 0.6648–0.68045 | 0 | 1 |
| [ER5MG24_A12](#phase-er-mg-er5mg24-a12); _phase:er-mg:er5mg24-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–875.96 K, x(Mg) 0.82759–0.846 | 0 | 1 |
| [FCC_A1](#phase-er-mg-fcc-a1); _phase:er-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-er-mg-hcp-a3); _phase:er-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1813.75 K, x(Mg) 0–1 | 0 | 1 |
| [LIQUID](#phase-er-mg-liquid); _phase:er-mg:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 839.55–2500 K, x(Mg) 0–1 | 2 | 1 |

## BCC_A2 (Er–Mg)

- Id: `phase:er-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 944.85–1530 K, x(Mg) 0.14533–0.43804
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-mg:bcc-a2)

Names (3): _corpus: _corpus:phase:er-mg:bcc-a2  
_tdb: _tdb:ErMg-02Cac.tdb:A2_BCC, tdb:ErMg-02Cac.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ErMg-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ErMg-02Cac.tdb): A2_BCC, type code %B, sha256 `e4be248b91beab31…`

~~~~text
38: PHASE A2_BCC %B 2 1 3 !
39: CONST A2_BCC : ER MG : VA : !
~~~~

[ErMg-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ErMg-02Cac.tdb): BCC_A2, type code %B, sha256 `e4be248b91beab31…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : ER MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## B2_BCC (Er–Mg)

- Id: `phase:er-mg:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: ErMg-02Cac.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in ErMg-02Cac.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1530 K, x(Mg) 0.14533–0.62073
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-mg:bcc-b2)

Names (2): _corpus: _corpus:phase:er-mg:bcc-b2  
_tdb: _tdb:ErMg-02Cac.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[ErMg-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ErMg-02Cac.tdb): B2_BCC, type code %BO, sha256 `e4be248b91beab31…`

~~~~text
43: PHASE B2_BCC %BO 3 0.5 0.5 3 !
44: CONST B2_BCC : ER% MG : ER MG% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## C14_LAVES (Er–Mg)

- Id: `phase:er-mg:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in ErMg-02Cac.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–952.28 K, x(Mg) 0.6648–0.68045
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-mg:c14-laves)

Names (2): _corpus: _corpus:phase:er-mg:c14-laves  
_tdb: _tdb:ErMg-02Cac.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[ErMg-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ErMg-02Cac.tdb): C14_LAVES, type code %, sha256 `e4be248b91beab31…`

~~~~text
53: PHASE C14_LAVES % 2 2 1 !
54: CONST C14_LAVES : ER MG% : ER% MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## ER5MG24_A12 (Er–Mg)

- Id: `phase:er-mg:er5mg24-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–875.96 K, x(Mg) 0.82759–0.846
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-mg:er5mg24-a12)

Names (2): _corpus: _corpus:phase:er-mg:er5mg24-a12  
_tdb: _tdb:ErMg-02Cac.tdb:ER5MG24_A12  


### TDB models of ER5MG24_A12 (1): PHASE and CONSTITUENT statements as written

[ErMg-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ErMg-02Cac.tdb): ER5MG24_A12, type code %, sha256 `e4be248b91beab31…`

~~~~text
58: PHASE ER5MG24_A12 % 3 5 12 12 !
59: CONST ER5MG24_A12 : ER% MG : MG : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## FCC_A1 (Er–Mg)

- Id: `phase:er-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-mg:fcc-a1)

Names (2): _corpus: _corpus:phase:er-mg:fcc-a1  
_tdb: _tdb:ErMg-02Cac.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ErMg-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ErMg-02Cac.tdb): FCC_A1, type code %A, sha256 `e4be248b91beab31…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : ER MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## HCP_A3 (Er–Mg)

- Id: `phase:er-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1813.75 K, x(Mg) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-mg:hcp-a3)

Names (2): _corpus: _corpus:phase:er-mg:hcp-a3  
_tdb: _tdb:ErMg-02Cac.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ErMg-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ErMg-02Cac.tdb): HCP_A3, type code %A, sha256 `e4be248b91beab31…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : ER% MG% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_

## LIQUID (Er–Mg)

- Id: `phase:er-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 839.55–2500 K, x(Mg) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-mg:liquid)

Names (3): _corpus: _corpus:phase:er-mg:liquid  
_paper: _paper:10.1007/bf02667226:L  
_tdb: _tdb:ErMg-02Cac.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ErMg-02Cac.tdb](https://orchid-project.org/data/databases/sgte-binary/ErMg-02Cac.tdb): LIQUID, type code %, sha256 `e4be248b91beab31…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : ER MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497102770332199](https://doi.org/10.1361/105497102770332199) G. Cacciamani, A. Saccone, S. De Negri, R. Ferro, J. Phase Equilib., 23, 38-50(2002).  
_assessment that models this phase_
- [doi:10.1007/bf02667226](https://doi.org/10.1007/bf02667226) H. Okamoto, Er-Lu (Erbium-Lutetium), JPE 13, 676-677 (1992).  
_reports values for this phase_

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
