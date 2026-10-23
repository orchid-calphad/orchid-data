# F–K phases

> F–K system: 7 phases (tier A 4, liquid 2, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/F-K.html · Markdown: https://data.orchid-project.org/phases/pages/F-K.md

7 phases (tier A 4, liquid 2, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=F-K) · [full JSON](https://data.orchid-project.org/phases/systems/F-K.json) · [F–K system page](https://data.orchid-project.org/systems/F-K.html) · [Markdown](https://data.orchid-project.org/phases/pages/F-K.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the F–K system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-f-k-bcc-a2); _phase:f-k:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–336.52 K, x(F) 0–0 | 1 | 1 |
| [FCC_A1](#phase-f-k-fcc-a1); _phase:f-k:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-f-k-gas); _phase:f-k:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(F) 0–1 | 2 | 1 |
| [HCP_A3](#phase-f-k-hcp-a3); _phase:f-k:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-f-k-ion); _phase:f-k:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 336.52–1858.29 K, x(F) 0–0.5 | 0 | 1 |
| [KF_B1](#phase-f-k-kf-b1); _phase:f-k:kf-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1131 K, x(F) 0.5–0.5 | 5 | 1 |
| [LIQUID](#phase-f-k-liquid); _phase:f-k:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 6 | 1 |

## BCC_A2 (F–K)

- Id: `phase:f-k:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–336.52 K, x(F) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-k:bcc-a2)

Names (3): _corpus: _corpus:phase:f-k:bcc-a2  
_paper: _paper:10.1016/j.msea.2005.11.037:bcc  
_tdb: _tdb:KF-06Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[KF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KF-06Zha.tdb): BCC_A2, type code %B, sha256 `07ca7dab8fb54d1b…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (F–K)

- Id: `phase:f-k:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-k:fcc-a1)

Names (2): _corpus: _corpus:phase:f-k:fcc-a1  
_tdb: _tdb:KF-06Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[KF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KF-06Zha.tdb): FCC_A1, type code %A, sha256 `07ca7dab8fb54d1b…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase_

## GAS (F–K)

- Id: `phase:f-k:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(F) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-k:gas)

Names (3): _corpus: _corpus:phase:f-k:gas  
_paper: _paper:10.1016/j.msea.2005.11.037:Gas (P = 3 bar)  
_tdb: _tdb:KF-06Zha.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[KF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KF-06Zha.tdb): GAS, type code %, sha256 `07ca7dab8fb54d1b…`

~~~~text
57: PHASE GAS:G % 1 1 !
58: CONST GAS:G : F F2 K K2 KF K2F2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (F–K)

- Id: `phase:f-k:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-k:hcp-a3)

Names (2): _corpus: _corpus:phase:f-k:hcp-a3  
_tdb: _tdb:KF-06Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[KF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KF-06Zha.tdb): HCP_A3, type code %A, sha256 `07ca7dab8fb54d1b…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase_

## ION (F–K)

- Id: `phase:f-k:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 336.52–1858.29 K, x(F) 0–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-k:ion)

Names (2): _corpus: _corpus:phase:f-k:ion  
_tdb: _tdb:KF-06Zha.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[KF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KF-06Zha.tdb): ION, type code %, sha256 `07ca7dab8fb54d1b…`

~~~~text
31: PHASE ION:Y % 2 1 1 !
32: CONST ION:Y : K+1 : F-1 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase_

## KF_B1 (F–K)

- Id: `phase:f-k:kf-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1131 K, x(F) 0.5–0.5
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-k:kf-b1)

Names (3): _corpus: _corpus:phase:f-k:kf-b1  
_paper: _paper:10.1016/j.msea.2005.11.037:KF  
_tdb: _tdb:KF-06Zha.tdb:KF_B1  


### TDB models of KF_B1 (1): PHASE and CONSTITUENT statements as written

[KF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KF-06Zha.tdb): KF_B1, type code %, sha256 `07ca7dab8fb54d1b…`

~~~~text
54: PHASE KF_B1 % 2 1 1 !
55: CONST KF_B1 : K : F : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ja01607a016](https://doi.org/10.1021/ja01607a016) M. A. Bredig, J. W. Johnson, Wm. T. Smith, Miscibility of Liquid Metals with Salts. I. The Sodium-Sodium Halide Systems\<sup>1\</sup>, J. Am. Chem. Soc. 77, 307-312 (1955).  
_cited as the source of values for this phase_

## LIQUID (F–K)

- Id: `phase:f-k:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: K 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-k:liquid)

Names (6): _corpus: _corpus:phase:f-k:liquid  
_paper: _paper:10.1016/j.msea.2005.11.037:L2, paper:10.1016/j.msea.2005.11.037:Liquid, paper:10.1016/j.msea.2005.11.037:Liquid 1, paper:10.1016/j.msea.2005.11.037:liquid  
_tdb: _tdb:KF-06Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[KF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KF-06Zha.tdb): LIQUID, type code %, sha256 `07ca7dab8fb54d1b…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : K : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ja01607a016](https://doi.org/10.1021/ja01607a016) M. A. Bredig, J. W. Johnson, Wm. T. Smith, Miscibility of Liquid Metals with Salts. I. The Sodium-Sodium Halide Systems\<sup>1\</sup>, J. Am. Chem. Soc. 77, 307-312 (1955).  
_cited as the source of values for this phase_

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
