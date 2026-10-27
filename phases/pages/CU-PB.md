# Cu–Pb phases

> Cu–Pb system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-PB.html · Markdown: https://data.orchid-project.org/phases/pages/CU-PB.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-PB) · [full JSON](https://data.orchid-project.org/phases/systems/CU-PB.json) · [Cu–Pb system page](https://data.orchid-project.org/systems/CU-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Pb system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-pb-bcc-a2); _phase:cu-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-cu-pb-fcc-a1); _phase:cu-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2499.74 K, x(Pb) 0–1 | 24 | 4 |
| [HCP_A3](#phase-cu-pb-hcp-a3); _phase:cu-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 600–600 K, x(Pb) 0.15–0.75 | 0 | 4 |
| [LIQUID](#phase-cu-pb-liquid); _phase:cu-pb:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 599.41–2500 K, x(Pb) 0–1 | 46 | 4 |

## BCC_A2 (Cu–Pb)

- Id: `phase:cu-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pb:bcc-a2)

Names (5): _corpus: _corpus:phase:cu-pb:bcc-a2  
_tdb: _tdb:CuPb-00Wan.tdb:BCC_A2, tdb:CuPb-01Ond.tdb:BCC_A2, tdb:CuPb-13Vaa.tdb:BCC_A2, tdb:CuPb-86Hay-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[CuPb-00Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-00Wan.tdb): BCC_A2, type code %B, sha256 `325b09773e6921c6…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CU PB : VA : !
~~~~

[CuPb-01Ond.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-01Ond.tdb): BCC_A2, type code %B, sha256 `05b1425b6f848b48…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CU PB : VA : !
~~~~

[CuPb-13Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-13Vaa.tdb): BCC_A2, type code %B, sha256 `98775991a8aa6392…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CU PB : VA : !
~~~~

[CuPb-86Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-86Hay-LB.tdb): BCC_A2, type code %B, sha256 `f43832e2238dd6fd…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU PB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0364-5916(00)00020-1](https://doi.org/10.1016/S0364-5916%2800%2900020-1) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Calphad, 24, 149-67(2000).  
_assessment that models this phase_
- [doi:10.1034/j.1600-0692.2001.300507.x](https://doi.org/10.1034/j.1600-0692.2001.300507.x) B. Onderka, L. A. Zabdyr, A new critical assessment of the copper‐lead system, Scand Jof Metallurgy 30, 320-323 (2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-771108](https://doi.org/10.1515/ijmr-1986-771108) F.H. Hayes, H.L. Lukas, G. Effenberg, G. Petzow, Z. Metallkd., 77, 749-54(1986).  
_assessment that models this phase_
- [doi:10.3139/146.110876](https://doi.org/10.3139/146.110876) I. Vaajamo, H. Johto, P. Taskinen, Int. J. Mater. Res., 104, 372-76(2013).  
_assessment that models this phase_

## FCC_A1 (Cu–Pb)

- Id: `phase:cu-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2499.74 K, x(Pb) 0–1
- Literature: 24 values (24 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pb:fcc-a1)

Names (9): _corpus: _corpus:phase:cu-pb:fcc-a1  
_paper: _paper:10.1016/s0364-5916(00)00020-1:(Cu), paper:10.1016/s0364-5916(00)00020-1:(Pb), paper:10.1034/j.1600-0692.2001.300507.x:(Cu), paper:10.1034/j.1600-0692.2001.300507.x:(Pb)  
_tdb: _tdb:CuPb-00Wan.tdb:FCC_A1, tdb:CuPb-01Ond.tdb:FCC_A1, tdb:CuPb-13Vaa.tdb:FCC_A1, tdb:CuPb-86Hay-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CuPb-00Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-00Wan.tdb): FCC_A1, type code %A, sha256 `325b09773e6921c6…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CU PB : VA : !
~~~~

[CuPb-01Ond.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-01Ond.tdb): FCC_A1, type code %A, sha256 `05b1425b6f848b48…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CU PB : VA : !
~~~~

[CuPb-13Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-13Vaa.tdb): FCC_A1, type code %A, sha256 `98775991a8aa6392…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CU PB : VA : !
~~~~

[CuPb-86Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-86Hay-LB.tdb): FCC_A1, type code %A, sha256 `f43832e2238dd6fd…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU PB : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/S0364-5916(00)00020-1](https://doi.org/10.1016/S0364-5916%2800%2900020-1) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Calphad, 24, 149-67(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1034/j.1600-0692.2001.300507.x](https://doi.org/10.1034/j.1600-0692.2001.300507.x) B. Onderka, L. A. Zabdyr, A new critical assessment of the copper‐lead system, Scand Jof Metallurgy 30, 320-323 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1986-771108](https://doi.org/10.1515/ijmr-1986-771108) F.H. Hayes, H.L. Lukas, G. Effenberg, G. Petzow, Z. Metallkd., 77, 749-54(1986).  
_assessment that models this phase_
- [doi:10.3139/146.110876](https://doi.org/10.3139/146.110876) I. Vaajamo, H. Johto, P. Taskinen, Int. J. Mater. Res., 104, 372-76(2013).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(91)80126-4](https://doi.org/10.1016/0040-6031%2891%2980126-4) Teppo O, Niemela J, Taskinen P. Thermochimica Acta 1991: 185: 155.  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(86)90011-8](https://doi.org/10.1016/0364-5916%2886%2990011-8) Niemela J. CALPHAD 1986: 10: 77.  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Pb)

- Id: `phase:cu-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 600–600 K, x(Pb) 0.15–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pb:hcp-a3)

Names (5): _corpus: _corpus:phase:cu-pb:hcp-a3  
_tdb: _tdb:CuPb-00Wan.tdb:HCP_A3, tdb:CuPb-01Ond.tdb:HCP_A3, tdb:CuPb-13Vaa.tdb:HCP_A3, tdb:CuPb-86Hay-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CuPb-00Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-00Wan.tdb): HCP_A3, type code %A, sha256 `325b09773e6921c6…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CU PB : VA : !
~~~~

[CuPb-01Ond.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-01Ond.tdb): HCP_A3, type code %A, sha256 `05b1425b6f848b48…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CU PB : VA : !
~~~~

[CuPb-13Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-13Vaa.tdb): HCP_A3, type code %A, sha256 `98775991a8aa6392…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CU PB : VA : !
~~~~

[CuPb-86Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-86Hay-LB.tdb): HCP_A3, type code %A, sha256 `f43832e2238dd6fd…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU PB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0364-5916(00)00020-1](https://doi.org/10.1016/S0364-5916%2800%2900020-1) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Calphad, 24, 149-67(2000).  
_assessment that models this phase_
- [doi:10.1034/j.1600-0692.2001.300507.x](https://doi.org/10.1034/j.1600-0692.2001.300507.x) B. Onderka, L. A. Zabdyr, A new critical assessment of the copper‐lead system, Scand Jof Metallurgy 30, 320-323 (2001).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1986-771108](https://doi.org/10.1515/ijmr-1986-771108) F.H. Hayes, H.L. Lukas, G. Effenberg, G. Petzow, Z. Metallkd., 77, 749-54(1986).  
_assessment that models this phase_
- [doi:10.3139/146.110876](https://doi.org/10.3139/146.110876) I. Vaajamo, H. Johto, P. Taskinen, Int. J. Mater. Res., 104, 372-76(2013).  
_assessment that models this phase_

## LIQUID (Cu–Pb)

- Id: `phase:cu-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 599.41–2500 K, x(Pb) 0–1
- Literature: 46 values (46 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pb:liquid)

Names (8): _corpus: _corpus:phase:cu-pb:liquid  
_paper: _paper:10.1016/s0364-5916(00)00020-1:L, paper:10.1016/s0364-5916(00)00020-1:L2, paper:10.1034/j.1600-0692.2001.300507.x:L2  
_tdb: _tdb:CuPb-00Wan.tdb:LIQUID, tdb:CuPb-01Ond.tdb:LIQUID, tdb:CuPb-13Vaa.tdb:LIQUID, tdb:CuPb-86Hay-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CuPb-00Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-00Wan.tdb): LIQUID, type code %, sha256 `325b09773e6921c6…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CU PB : !
~~~~

[CuPb-01Ond.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-01Ond.tdb): LIQUID, type code %, sha256 `05b1425b6f848b48…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CU PB : !
~~~~

[CuPb-13Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-13Vaa.tdb): LIQUID, type code %, sha256 `98775991a8aa6392…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CU PB : !
~~~~

[CuPb-86Hay-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPb-86Hay-LB.tdb): LIQUID, type code %, sha256 `f43832e2238dd6fd…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CU PB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/S0364-5916(00)00020-1](https://doi.org/10.1016/S0364-5916%2800%2900020-1) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Calphad, 24, 149-67(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1034/j.1600-0692.2001.300507.x](https://doi.org/10.1034/j.1600-0692.2001.300507.x) B. Onderka, L. A. Zabdyr, A new critical assessment of the copper‐lead system, Scand Jof Metallurgy 30, 320-323 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1986-771108](https://doi.org/10.1515/ijmr-1986-771108) F.H. Hayes, H.L. Lukas, G. Effenberg, G. Petzow, Z. Metallkd., 77, 749-54(1986).  
_assessment that models this phase_
- [doi:10.3139/146.110876](https://doi.org/10.3139/146.110876) I. Vaajamo, H. Johto, P. Taskinen, Int. J. Mater. Res., 104, 372-76(2013).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(91)80126-4](https://doi.org/10.1016/0040-6031%2891%2980126-4) Teppo O, Niemela J, Taskinen P. Thermochimica Acta 1991: 185: 155.  
_cited as the source of values for this phase_
- [doi:10.1016/0364-5916(86)90011-8](https://doi.org/10.1016/0364-5916%2886%2990011-8) Niemela J. CALPHAD 1986: 10: 77.  
_cited as the source of values for this phase_

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
