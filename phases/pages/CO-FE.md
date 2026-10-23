# Co–Fe phases

> Co–Fe system: 5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-FE.html · Markdown: https://data.orchid-project.org/phases/pages/CO-FE.md

5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-FE) · [full JSON](https://data.orchid-project.org/phases/systems/CO-FE.json) · [Co–Fe system page](https://data.orchid-project.org/systems/CO-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Fe system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-fe-bcc-a2); _phase:co-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 6 calculated diagram(s): 300–1810.95 K, x(Fe) 0.18484–1 | 0 | 6 |
| [B2_BCC](#phase-co-fe-bcc-b2); _phase:co-fe:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1810.95 K, x(Fe) 0.23523–1 | 0 | 2 |
| [FCC_A1](#phase-co-fe-fcc-a1); _phase:co-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 406.16–1777.77 K, x(Fe) 0–1 | 0 | 4 |
| [HCP_A3](#phase-co-fe-hcp-a3); _phase:co-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–779.98 K, x(Fe) 0–0.03623 | 0 | 4 |
| [LIQUID](#phase-co-fe-liquid); _phase:co-fe:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1745.93–2500 K, x(Fe) 0–1 | 0 | 4 |

## BCC_A2 (Co–Fe)

- Id: `phase:co-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 6 calculated diagram(s): 300–1810.95 K, x(Fe) 0.18484–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-fe:bcc-a2)

Names (7): _corpus: _corpus:phase:co-fe:bcc-a2  
_tdb: _tdb:CoFe-02Ohn.tdb:A2_BCC, tdb:CoFe-02Ohn.tdb:BCC_A2, tdb:CoFe-15Rod.tdb:BCC_A2, tdb:CoFe-17Wan.tdb:A2_BCC, tdb:CoFe-17Wan.tdb:BCC_A2, tdb:CoFe-87Fer-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[CoFe-02Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-02Ohn.tdb): A2_BCC, type code %B, sha256 `4ed3ddb5c0d6db77…`

~~~~text
40: PHASE A2_BCC %B 2 1 3 !
41: CONST A2_BCC : CO FE : VA : !
~~~~

[CoFe-02Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-02Ohn.tdb): BCC_A2, type code %B, sha256 `4ed3ddb5c0d6db77…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CO FE% : VA : !
~~~~

[CoFe-15Rod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-15Rod.tdb): BCC_A2, type code %B, sha256 `b439f24ad16996c6…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO FE% : VA : !
~~~~

[CoFe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-17Wan.tdb): A2_BCC, type code %B, sha256 `324b5028ec03d395…`

~~~~text
37: PHASE A2_BCC %B 2 1 3 !
38: CONST A2_BCC : CO FE : VA : !
~~~~

[CoFe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-17Wan.tdb): BCC_A2, type code %B, sha256 `324b5028ec03d395…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CO FE% : VA : !
~~~~

[CoFe-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-87Fer-LB.tdb): BCC_A2, type code %B, sha256 `edf9a6fc99f8e55a…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CO FE% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.03.001](https://doi.org/10.1016/j.calphad.2015.03.001) Justin E. Rodriguez, Douglas M. Matson, Thermodynamic modeling of the solidification path of levitated Fe–Co alloys, Calphad 49, 87-100 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.06.001](https://doi.org/10.1016/j.calphad.2017.06.001) J. Wang, X.-G. Lu, N. Zhu, W. Zheng, Calphad, 58, 82-100(2017).  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(01)00337-8](https://doi.org/10.1016/S1359-6454%2801%2900337-8) I. Ohnuma, H. Enoki, O. Ikeda, R. Kainuma, H. Ohtani, B. Sundman, K. Ishida, Acta Mater., 50, 379-93(2002).  
_assessment that models this phase_

## B2_BCC (Co–Fe)

- Id: `phase:co-fe:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: CoFe-02Ohn.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: CoFe-17Wan.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in CoFe-02Ohn.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoFe-17Wan.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–1810.95 K, x(Fe) 0.23523–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-fe:bcc-b2)

Names (3): _corpus: _corpus:phase:co-fe:bcc-b2  
_tdb: _tdb:CoFe-02Ohn.tdb:B2_BCC, tdb:CoFe-17Wan.tdb:B2_BCC  


### TDB models of B2_BCC (2): PHASE and CONSTITUENT statements as written

[CoFe-02Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-02Ohn.tdb): B2_BCC, type code %BO, sha256 `4ed3ddb5c0d6db77…`

~~~~text
45: PHASE B2_BCC %BO 3 0.5 0.5 3 !
46: CONST B2_BCC : CO% FE : CO FE% : VA : !
~~~~

[CoFe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-17Wan.tdb): B2_BCC, type code %BO, sha256 `324b5028ec03d395…`

~~~~text
42: PHASE B2_BCC %BO 3 0.5 0.5 3 !
43: CONST B2_BCC : CO% FE : CO FE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2017.06.001](https://doi.org/10.1016/j.calphad.2017.06.001) J. Wang, X.-G. Lu, N. Zhu, W. Zheng, Calphad, 58, 82-100(2017).  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(01)00337-8](https://doi.org/10.1016/S1359-6454%2801%2900337-8) I. Ohnuma, H. Enoki, O. Ikeda, R. Kainuma, H. Ohtani, B. Sundman, K. Ishida, Acta Mater., 50, 379-93(2002).  
_assessment that models this phase_

## FCC_A1 (Co–Fe)

- Id: `phase:co-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 406.16–1777.77 K, x(Fe) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-fe:fcc-a1)

Names (5): _corpus: _corpus:phase:co-fe:fcc-a1  
_tdb: _tdb:CoFe-02Ohn.tdb:FCC_A1, tdb:CoFe-15Rod.tdb:FCC_A1, tdb:CoFe-17Wan.tdb:FCC_A1, tdb:CoFe-87Fer-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CoFe-02Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-02Ohn.tdb): FCC_A1, type code %A, sha256 `4ed3ddb5c0d6db77…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CO% FE% : VA : !
~~~~

[CoFe-15Rod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-15Rod.tdb): FCC_A1, type code %A, sha256 `b439f24ad16996c6…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% FE% : VA : !
~~~~

[CoFe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-17Wan.tdb): FCC_A1, type code %A, sha256 `324b5028ec03d395…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% FE% : VA : !
~~~~

[CoFe-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-87Fer-LB.tdb): FCC_A1, type code %A, sha256 `edf9a6fc99f8e55a…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CO% FE% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.03.001](https://doi.org/10.1016/j.calphad.2015.03.001) Justin E. Rodriguez, Douglas M. Matson, Thermodynamic modeling of the solidification path of levitated Fe–Co alloys, Calphad 49, 87-100 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.06.001](https://doi.org/10.1016/j.calphad.2017.06.001) J. Wang, X.-G. Lu, N. Zhu, W. Zheng, Calphad, 58, 82-100(2017).  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(01)00337-8](https://doi.org/10.1016/S1359-6454%2801%2900337-8) I. Ohnuma, H. Enoki, O. Ikeda, R. Kainuma, H. Ohtani, B. Sundman, K. Ishida, Acta Mater., 50, 379-93(2002).  
_assessment that models this phase_

## HCP_A3 (Co–Fe)

- Id: `phase:co-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–779.98 K, x(Fe) 0–0.03623
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-fe:hcp-a3)

Names (5): _corpus: _corpus:phase:co-fe:hcp-a3  
_tdb: _tdb:CoFe-02Ohn.tdb:HCP_A3, tdb:CoFe-15Rod.tdb:HCP_A3, tdb:CoFe-17Wan.tdb:HCP_A3, tdb:CoFe-87Fer-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CoFe-02Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-02Ohn.tdb): HCP_A3, type code %A, sha256 `4ed3ddb5c0d6db77…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : CO% FE : VA : !
~~~~

[CoFe-15Rod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-15Rod.tdb): HCP_A3, type code %A, sha256 `b439f24ad16996c6…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% FE : VA : !
~~~~

[CoFe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-17Wan.tdb): HCP_A3, type code %A, sha256 `324b5028ec03d395…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : CO% FE : VA : !
~~~~

[CoFe-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-87Fer-LB.tdb): HCP_A3, type code %A, sha256 `edf9a6fc99f8e55a…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CO% FE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.03.001](https://doi.org/10.1016/j.calphad.2015.03.001) Justin E. Rodriguez, Douglas M. Matson, Thermodynamic modeling of the solidification path of levitated Fe–Co alloys, Calphad 49, 87-100 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.06.001](https://doi.org/10.1016/j.calphad.2017.06.001) J. Wang, X.-G. Lu, N. Zhu, W. Zheng, Calphad, 58, 82-100(2017).  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(01)00337-8](https://doi.org/10.1016/S1359-6454%2801%2900337-8) I. Ohnuma, H. Enoki, O. Ikeda, R. Kainuma, H. Ohtani, B. Sundman, K. Ishida, Acta Mater., 50, 379-93(2002).  
_assessment that models this phase_

## LIQUID (Co–Fe)

- Id: `phase:co-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1745.93–2500 K, x(Fe) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-fe:liquid)

Names (5): _corpus: _corpus:phase:co-fe:liquid  
_tdb: _tdb:CoFe-02Ohn.tdb:LIQUID, tdb:CoFe-15Rod.tdb:LIQUID, tdb:CoFe-17Wan.tdb:LIQUID, tdb:CoFe-87Fer-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CoFe-02Ohn.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-02Ohn.tdb): LIQUID, type code %, sha256 `4ed3ddb5c0d6db77…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CO FE : !
~~~~

[CoFe-15Rod.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-15Rod.tdb): LIQUID, type code %, sha256 `b439f24ad16996c6…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO FE : !
~~~~

[CoFe-17Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-17Wan.tdb): LIQUID, type code %, sha256 `324b5028ec03d395…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO FE : !
~~~~

[CoFe-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoFe-87Fer-LB.tdb): LIQUID, type code %, sha256 `edf9a6fc99f8e55a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CO FE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2015.03.001](https://doi.org/10.1016/j.calphad.2015.03.001) Justin E. Rodriguez, Douglas M. Matson, Thermodynamic modeling of the solidification path of levitated Fe–Co alloys, Calphad 49, 87-100 (2015).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.06.001](https://doi.org/10.1016/j.calphad.2017.06.001) J. Wang, X.-G. Lu, N. Zhu, W. Zheng, Calphad, 58, 82-100(2017).  
_assessment that models this phase_
- [doi:10.1016/S1359-6454(01)00337-8](https://doi.org/10.1016/S1359-6454%2801%2900337-8) I. Ohnuma, H. Enoki, O. Ikeda, R. Kainuma, H. Ohtani, B. Sundman, K. Ishida, Acta Mater., 50, 379-93(2002).  
_assessment that models this phase_

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
