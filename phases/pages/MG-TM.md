# Mg–Tm phases

> Mg–Tm system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MG-TM.html · Markdown: https://data.orchid-project.org/phases/pages/MG-TM.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MG-TM) · [full JSON](https://data.orchid-project.org/phases/systems/MG-TM.json) · [Mg–Tm system page](https://data.orchid-project.org/systems/MG-TM.html) · [Markdown](https://data.orchid-project.org/phases/pages/MG-TM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mg–Tm system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mg-tm-bcc-a2); _phase:mg-tm:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 943.44–1473.23 K, x(Tm) 0.55888–0.75122 | 6 | 1 |
| [FCC_A1](#phase-mg-tm-fcc-a1); _phase:mg-tm:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-mg-tm-hcp-a3); _phase:mg-tm:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.24 K, x(Tm) 0–1 | 6 | 1 |
| [LIQUID](#phase-mg-tm-liquid); _phase:mg-tm:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 847.99–2500 K, x(Tm) 0–1 | 10 | 1 |
| [MG24TM5_A12](#phase-mg-tm-mg24tm5-a12); _phase:mg-tm:mg24tm5-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–863.07 K, x(Tm) 0.17241–0.17241 | 4 | 1 |
| [MG2TM_C14](#phase-mg-tm-mg2tm-c14); _phase:mg-tm:mg2tm-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.04 K, x(Tm) 0.33333–0.33333 | 4 | 1 |
| [MGTM_B2](#phase-mg-tm-mgtm-b2); _phase:mg-tm:mgtm-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1033.21 K, x(Tm) 0.41162–0.51997 | 6 | 1 |

## BCC_A2 (Mg–Tm)

- Id: `phase:mg-tm:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 943.44–1473.23 K, x(Tm) 0.55888–0.75122
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tm:bcc-a2)

Names (3): _corpus: _corpus:phase:mg-tm:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2003.10.033:bcc  
_tdb: _tdb:MgTm-04Du-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MgTm-04Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTm-04Du-LB.tdb): BCC_A2, type code %B, sha256 `8bc07bc38ca74452…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MG TM : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033) Zhenmin Du, Hongying Liu, Gang Ling, Thermodynamic assessment of the Mg–Tm system, Journal of Alloys and Compounds 373, 151-155 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06023-1](https://doi.org/10.1016/0925-8388%2894%2906023-1) A. Saccone, D. Macciò, S. Delfino, R. Ferro, The interpolated TmMg phase diagram, Journal of Alloys and Compounds 220, 161-166 (1995).  
_cited as the source of values for this phase_

## FCC_A1 (Mg–Tm)

- Id: `phase:mg-tm:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tm:fcc-a1)

Names (2): _corpus: _corpus:phase:mg-tm:fcc-a1  
_tdb: _tdb:MgTm-04Du-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MgTm-04Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTm-04Du-LB.tdb): FCC_A1, type code %A, sha256 `8bc07bc38ca74452…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033) Zhenmin Du, Hongying Liu, Gang Ling, Thermodynamic assessment of the Mg–Tm system, Journal of Alloys and Compounds 373, 151-155 (2004).  
_assessment that models this phase_

## HCP_A3 (Mg–Tm)

- Id: `phase:mg-tm:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.24 K, x(Tm) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tm:hcp-a3)

Names (4): _corpus: _corpus:phase:mg-tm:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2003.10.033:hcp(Mg), paper:10.1016/j.jallcom.2003.10.033:hcp(Tm)  
_tdb: _tdb:MgTm-04Du-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MgTm-04Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTm-04Du-LB.tdb): HCP_A3, type code %A, sha256 `8bc07bc38ca74452…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MG TM : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033) Zhenmin Du, Hongying Liu, Gang Ling, Thermodynamic assessment of the Mg–Tm system, Journal of Alloys and Compounds 373, 151-155 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06023-1](https://doi.org/10.1016/0925-8388%2894%2906023-1) A. Saccone, D. Macciò, S. Delfino, R. Ferro, The interpolated TmMg phase diagram, Journal of Alloys and Compounds 220, 161-166 (1995).  
_cited as the source of values for this phase_

## LIQUID (Mg–Tm)

- Id: `phase:mg-tm:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 847.99–2500 K, x(Tm) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tm:liquid)

Names (3): _corpus: _corpus:phase:mg-tm:liquid  
_paper: _paper:10.1016/j.jallcom.2003.10.033:liquid  
_tdb: _tdb:MgTm-04Du-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MgTm-04Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTm-04Du-LB.tdb): LIQUID, type code %, sha256 `8bc07bc38ca74452…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MG TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033) Zhenmin Du, Hongying Liu, Gang Ling, Thermodynamic assessment of the Mg–Tm system, Journal of Alloys and Compounds 373, 151-155 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06023-1](https://doi.org/10.1016/0925-8388%2894%2906023-1) A. Saccone, D. Macciò, S. Delfino, R. Ferro, The interpolated TmMg phase diagram, Journal of Alloys and Compounds 220, 161-166 (1995).  
_cited as the source of values for this phase_

## MG24TM5_A12 (Mg–Tm)

- Id: `phase:mg-tm:mg24tm5-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 0.8276, Tm 0.1724
- Stability: stable in 1 of 1 calculated diagram(s): 300–863.07 K, x(Tm) 0.17241–0.17241
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tm:mg24tm5-a12)

Names (3): _corpus: _corpus:phase:mg-tm:mg24tm5-a12  
_paper: _paper:10.1016/j.jallcom.2003.10.033:Mg24Tm5  
_tdb: _tdb:MgTm-04Du-LB.tdb:MG24TM5_A12  


### TDB models of MG24TM5_A12 (1): PHASE and CONSTITUENT statements as written

[MgTm-04Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTm-04Du-LB.tdb): MG24TM5_A12, type code %, sha256 `8bc07bc38ca74452…`

~~~~text
41: PHASE MG24TM5_A12 % 2 24 5 !
42: CONST MG24TM5_A12 : MG : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033) Zhenmin Du, Hongying Liu, Gang Ling, Thermodynamic assessment of the Mg–Tm system, Journal of Alloys and Compounds 373, 151-155 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06023-1](https://doi.org/10.1016/0925-8388%2894%2906023-1) A. Saccone, D. Macciò, S. Delfino, R. Ferro, The interpolated TmMg phase diagram, Journal of Alloys and Compounds 220, 161-166 (1995).  
_cited as the source of values for this phase_

## MG2TM_C14 (Mg–Tm)

- Id: `phase:mg-tm:mg2tm-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 0.6667, Tm 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.04 K, x(Tm) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tm:mg2tm-c14)

Names (3): _corpus: _corpus:phase:mg-tm:mg2tm-c14  
_paper: _paper:10.1016/j.jallcom.2003.10.033:Mg2Tm  
_tdb: _tdb:MgTm-04Du-LB.tdb:MG2TM_C14  


### TDB models of MG2TM_C14 (1): PHASE and CONSTITUENT statements as written

[MgTm-04Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTm-04Du-LB.tdb): MG2TM_C14, type code %, sha256 `8bc07bc38ca74452…`

~~~~text
46: PHASE MG2TM_C14 % 2 2 1 !
47: CONST MG2TM_C14 : MG : TM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033) Zhenmin Du, Hongying Liu, Gang Ling, Thermodynamic assessment of the Mg–Tm system, Journal of Alloys and Compounds 373, 151-155 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06023-1](https://doi.org/10.1016/0925-8388%2894%2906023-1) A. Saccone, D. Macciò, S. Delfino, R. Ferro, The interpolated TmMg phase diagram, Journal of Alloys and Compounds 220, 161-166 (1995).  
_cited as the source of values for this phase_

## MGTM_B2 (Mg–Tm)

- Id: `phase:mg-tm:mgtm-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1033.21 K, x(Tm) 0.41162–0.51997
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mg-tm:mgtm-b2)

Names (3): _corpus: _corpus:phase:mg-tm:mgtm-b2  
_paper: _paper:10.1016/j.jallcom.2003.10.033:MgTm  
_tdb: _tdb:MgTm-04Du-LB.tdb:MGTM_B2  


### TDB models of MGTM_B2 (1): PHASE and CONSTITUENT statements as written

[MgTm-04Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MgTm-04Du-LB.tdb): MGTM_B2, type code %, sha256 `8bc07bc38ca74452…`

~~~~text
51: PHASE MGTM_B2 % 2 1 1 !
52: CONST MGTM_B2 : MG% VA : MG TM% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.033](https://doi.org/10.1016/j.jallcom.2003.10.033) Zhenmin Du, Hongying Liu, Gang Ling, Thermodynamic assessment of the Mg–Tm system, Journal of Alloys and Compounds 373, 151-155 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(94)06023-1](https://doi.org/10.1016/0925-8388%2894%2906023-1) A. Saccone, D. Macciò, S. Delfino, R. Ferro, The interpolated TmMg phase diagram, Journal of Alloys and Compounds 220, 161-166 (1995).  
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
