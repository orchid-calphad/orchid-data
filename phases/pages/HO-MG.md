# Ho–Mg phases

> Ho–Mg system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HO-MG.html · Markdown: https://data.orchid-project.org/phases/pages/HO-MG.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HO-MG) · [full JSON](https://data.orchid-project.org/phases/systems/HO-MG.json) · [Ho–Mg system page](https://data.orchid-project.org/systems/HO-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/HO-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ho–Mg system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ho-mg-bcc-a2); _phase:ho-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 958.15–1600 K, x(Mg) 0.08–0.42442 | 0 | 4 |
| [B2_BCC](#phase-ho-mg-bcc-b2); _phase:ho-mg:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1625.33 K, x(Mg) 0.06164–0.62095 | 0 | 2 |
| [C14_LAVES](#phase-ho-mg-c14-laves); _phase:ho-mg:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–967.06 K, x(Mg) 0.64097–0.6858 | 0 | 2 |
| [FCC_A1](#phase-ho-mg-fcc-a1); _phase:ho-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ho-mg-hcp-a3); _phase:ho-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1753.18 K, x(Mg) 0–1 | 0 | 2 |
| [HO5MG24_A12](#phase-ho-mg-ho5mg24-a12); _phase:ho-mg:ho5mg24-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–862.27 K, x(Mg) 0.82759–0.84828 | 0 | 2 |
| [LIQUID](#phase-ho-mg-liquid); _phase:ho-mg:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 842.88–2500 K, x(Mg) 0–1 | 0 | 2 |

## BCC_A2 (Ho–Mg)

- Id: `phase:ho-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 958.15–1600 K, x(Mg) 0.08–0.42442
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mg:bcc-a2)

Names (5): _corpus: _corpus:phase:ho-mg:bcc-a2  
_tdb: _tdb:HoMg-03Cac-LB.tdb:A2_BCC, tdb:HoMg-03Cac-LB.tdb:BCC_A2, tdb:HoMg-13Tok.tdb:A2_BCC, tdb:HoMg-13Tok.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[HoMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-03Cac-LB.tdb): A2_BCC, type code %B, sha256 `b1d78ae01625f0f3…`

~~~~text
36: PHASE A2_BCC %B 2 1 3 !
37: CONST A2_BCC : HO MG : VA : !
~~~~

[HoMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-03Cac-LB.tdb): BCC_A2, type code %B, sha256 `b1d78ae01625f0f3…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : HO MG : VA : !
~~~~

[HoMg-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-13Tok.tdb): A2_BCC, type code %B, sha256 `e7b08f0b3a66762f…`

~~~~text
41: PHASE A2_BCC %B 2 1 3 !
42: CONST A2_BCC : HO MG : VA : !
~~~~

[HoMg-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-13Tok.tdb): BCC_A2, type code %B, sha256 `e7b08f0b3a66762f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : HO MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## B2_BCC (Ho–Mg)

- Id: `phase:ho-mg:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: HoMg-03Cac-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: HoMg-13Tok.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in HoMg-03Cac-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in HoMg-13Tok.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1625.33 K, x(Mg) 0.06164–0.62095
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mg:bcc-b2)

Names (3): _corpus: _corpus:phase:ho-mg:bcc-b2  
_tdb: _tdb:HoMg-03Cac-LB.tdb:B2_BCC, tdb:HoMg-13Tok.tdb:B2_BCC  


### TDB models of B2_BCC (2): PHASE and CONSTITUENT statements as written

[HoMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-03Cac-LB.tdb): B2_BCC, type code %O, sha256 `b1d78ae01625f0f3…`

~~~~text
41: PHASE B2_BCC %O 3 0.5 0.5 3 !
42: CONST B2_BCC : HO% MG : HO MG% : VA : !
~~~~

[HoMg-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-13Tok.tdb): B2_BCC, type code %O, sha256 `e7b08f0b3a66762f…`

~~~~text
46: PHASE B2_BCC %O 3 0.5 0.5 3 !
47: CONST B2_BCC : HO% MG : HO MG% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## C14_LAVES (Ho–Mg)

- Id: `phase:ho-mg:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HoMg-03Cac-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in HoMg-13Tok.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–967.06 K, x(Mg) 0.64097–0.6858
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mg:c14-laves)

Names (3): _corpus: _corpus:phase:ho-mg:c14-laves  
_tdb: _tdb:HoMg-03Cac-LB.tdb:C14_LAVES, tdb:HoMg-13Tok.tdb:C14_LAVES  


### TDB models of C14_LAVES (2): PHASE and CONSTITUENT statements as written

[HoMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-03Cac-LB.tdb): C14_LAVES, type code %, sha256 `b1d78ae01625f0f3…`

~~~~text
51: PHASE C14_LAVES % 2 2 1 !
52: CONST C14_LAVES : HO MG% : HO% MG : !
~~~~

[HoMg-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-13Tok.tdb): C14_LAVES, type code %, sha256 `e7b08f0b3a66762f…`

~~~~text
56: PHASE C14_LAVES % 2 2 1 !
57: CONST C14_LAVES : HO MG% : HO% MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## FCC_A1 (Ho–Mg)

- Id: `phase:ho-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mg:fcc-a1)

Names (3): _corpus: _corpus:phase:ho-mg:fcc-a1  
_tdb: _tdb:HoMg-03Cac-LB.tdb:FCC_A1, tdb:HoMg-13Tok.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HoMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-03Cac-LB.tdb): FCC_A1, type code %A, sha256 `b1d78ae01625f0f3…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : HO MG : VA : !
~~~~

[HoMg-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-13Tok.tdb): FCC_A1, type code %A, sha256 `e7b08f0b3a66762f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : HO MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## HCP_A3 (Ho–Mg)

- Id: `phase:ho-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1753.18 K, x(Mg) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mg:hcp-a3)

Names (3): _corpus: _corpus:phase:ho-mg:hcp-a3  
_tdb: _tdb:HoMg-03Cac-LB.tdb:HCP_A3, tdb:HoMg-13Tok.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HoMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-03Cac-LB.tdb): HCP_A3, type code %A, sha256 `b1d78ae01625f0f3…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : HO MG : VA : !
~~~~

[HoMg-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-13Tok.tdb): HCP_A3, type code %A, sha256 `e7b08f0b3a66762f…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : HO MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## HO5MG24_A12 (Ho–Mg)

- Id: `phase:ho-mg:ho5mg24-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–862.27 K, x(Mg) 0.82759–0.84828
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mg:ho5mg24-a12)

Names (3): _corpus: _corpus:phase:ho-mg:ho5mg24-a12  
_tdb: _tdb:HoMg-03Cac-LB.tdb:HO5MG24_A12, tdb:HoMg-13Tok.tdb:HO5MG24_A12  


### TDB models of HO5MG24_A12 (2): PHASE and CONSTITUENT statements as written

[HoMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-03Cac-LB.tdb): HO5MG24_A12, type code %, sha256 `b1d78ae01625f0f3…`

~~~~text
56: PHASE HO5MG24_A12 % 3 5 12 12 !
57: CONST HO5MG24_A12 : HO% MG : MG : MG : !
~~~~

[HoMg-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-13Tok.tdb): HO5MG24_A12, type code %, sha256 `e7b08f0b3a66762f…`

~~~~text
61: PHASE HO5MG24_A12 % 3 5 12 12 !
62: CONST HO5MG24_A12 : HO% MG : MG : MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## LIQUID (Ho–Mg)

- Id: `phase:ho-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 842.88–2500 K, x(Mg) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mg:liquid)

Names (3): _corpus: _corpus:phase:ho-mg:liquid  
_tdb: _tdb:HoMg-03Cac-LB.tdb:LIQUID, tdb:HoMg-13Tok.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HoMg-03Cac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-03Cac-LB.tdb): LIQUID, type code %, sha256 `b1d78ae01625f0f3…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : HO MG : !
~~~~

[HoMg-13Tok.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMg-13Tok.tdb): LIQUID, type code %, sha256 `e7b08f0b3a66762f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : HO MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0966-9795(03)00151-1](https://doi.org/10.1016/S0966-9795%2803%2900151-1) G. Cacciamani, S. De Negri, A. Saccone, R. Ferro, Intermetallics, 11, 1135-51(2003).  
_assessment that models this phase_
- [doi:10.2320/matertrans.MI201226](https://doi.org/10.2320/matertrans.MI201226) T. Tokunaga, H. Kominato, S. Iikubo, H. Ohtani, Mater. Trans. (JIM), 54, 647-55(2013).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
