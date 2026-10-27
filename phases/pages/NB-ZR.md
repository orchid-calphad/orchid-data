# Nb–Zr phases

> Nb–Zr system: 7 phases (tier A 6, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/NB-ZR.md

7 phases (tier A 6, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/NB-ZR.json) · [Nb–Zr system page](https://data.orchid-project.org/systems/NB-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–Zr system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nb-zr-bcc-a2); _phase:nb-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.1 K, x(Zr) 0–1 | 0 | 2 |
| [C14_LAVES](#phase-nb-zr-c14-laves); _phase:nb-zr:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [C15_LAVES](#phase-nb-zr-c15-laves); _phase:nb-zr:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [C36_LAVES](#phase-nb-zr-c36-laves); _phase:nb-zr:c36-laves_ | MgNi2 · C36 · hP24 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-nb-zr-fcc-a1); _phase:nb-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-nb-zr-hcp-a3); _phase:nb-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2743.99 K, x(Zr) 0.99282–1 | 0 | 2 |
| [LIQUID](#phase-nb-zr-liquid); _phase:nb-zr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2016.15–4000 K, x(Zr) 0–1 | 0 | 2 |

## BCC_A2 (Nb–Zr)

- Id: `phase:nb-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.1 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zr:bcc-a2)

Names (3): _corpus: _corpus:phase:nb-zr:bcc-a2  
_tdb: _tdb:NbZr-19Laf.tdb:BCC_A2, tdb:NbZr-91Fer-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NbZr-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-19Laf.tdb): BCC_A2, type code %B, sha256 `a42c533c5325c028…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NB ZR : VA : !
~~~~

[NbZr-91Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-91Fer-LB.tdb): BCC_A2, type code %B, sha256 `7909b901df4293ef…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NB ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820609](https://doi.org/10.1515/ijmr-1991-820609) A. Fernandez Guillermet, Z. Metallkd., 82, 478-87(1991).  
_assessment that models this phase_

## C14_LAVES (Nb–Zr)

- Id: `phase:nb-zr:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NbZr-19Laf.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zr:c14-laves)

Names (2): _corpus: _corpus:phase:nb-zr:c14-laves  
_tdb: _tdb:NbZr-19Laf.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[NbZr-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-19Laf.tdb): C14_LAVES, type code %, sha256 `a42c533c5325c028…`

~~~~text
43: PHASE C14_LAVES % 3 4 2 6 !
44: CONST C14_LAVES : NB ZR : NB ZR : NB ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_

## C15_LAVES (Nb–Zr)

- Id: `phase:nb-zr:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NbZr-19Laf.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zr:c15-laves)

Names (2): _corpus: _corpus:phase:nb-zr:c15-laves  
_tdb: _tdb:NbZr-19Laf.tdb:C15_LAVES  


### TDB models of C15_LAVES (1): PHASE and CONSTITUENT statements as written

[NbZr-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-19Laf.tdb): C15_LAVES, type code %, sha256 `a42c533c5325c028…`

~~~~text
48: PHASE C15_LAVES % 2 2 1 !
49: CONST C15_LAVES : NB ZR : NB ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_

## C36_LAVES (Nb–Zr)

- Id: `phase:nb-zr:c36-laves`; status `assigned`
- Structure: MgNi2 · C36 · hP24 · P6_3/mmc (194); type `st:c36-mgni2-hp24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NbZr-19Laf.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zr:c36-laves)

Names (2): _corpus: _corpus:phase:nb-zr:c36-laves  
_tdb: _tdb:NbZr-19Laf.tdb:C36_LAVES  


### TDB models of C36_LAVES (1): PHASE and CONSTITUENT statements as written

[NbZr-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-19Laf.tdb): C36_LAVES, type code %, sha256 `a42c533c5325c028…`

~~~~text
53: PHASE C36_LAVES % 3 4 4 16 !
54: CONST C36_LAVES : NB ZR : NB ZR : NB ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_

## FCC_A1 (Nb–Zr)

- Id: `phase:nb-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zr:fcc-a1)

Names (3): _corpus: _corpus:phase:nb-zr:fcc-a1  
_tdb: _tdb:NbZr-19Laf.tdb:FCC_A1, tdb:NbZr-91Fer-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NbZr-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-19Laf.tdb): FCC_A1, type code %A, sha256 `a42c533c5325c028…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NB ZR : VA : !
~~~~

[NbZr-91Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-91Fer-LB.tdb): FCC_A1, type code %A, sha256 `7909b901df4293ef…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NB ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820609](https://doi.org/10.1515/ijmr-1991-820609) A. Fernandez Guillermet, Z. Metallkd., 82, 478-87(1991).  
_assessment that models this phase_

## HCP_A3 (Nb–Zr)

- Id: `phase:nb-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2743.99 K, x(Zr) 0.99282–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zr:hcp-a3)

Names (3): _corpus: _corpus:phase:nb-zr:hcp-a3  
_tdb: _tdb:NbZr-19Laf.tdb:HCP_A3, tdb:NbZr-91Fer-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NbZr-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-19Laf.tdb): HCP_A3, type code %A, sha256 `a42c533c5325c028…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NB ZR : VA : !
~~~~

[NbZr-91Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-91Fer-LB.tdb): HCP_A3, type code %A, sha256 `7909b901df4293ef…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NB ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820609](https://doi.org/10.1515/ijmr-1991-820609) A. Fernandez Guillermet, Z. Metallkd., 82, 478-87(1991).  
_assessment that models this phase_

## LIQUID (Nb–Zr)

- Id: `phase:nb-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2016.15–4000 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-zr:liquid)

Names (3): _corpus: _corpus:phase:nb-zr:liquid  
_tdb: _tdb:NbZr-19Laf.tdb:LIQUID, tdb:NbZr-91Fer-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NbZr-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-19Laf.tdb): LIQUID, type code %, sha256 `a42c533c5325c028…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NB ZR : !
~~~~

[NbZr-91Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbZr-91Fer-LB.tdb): LIQUID, type code %, sha256 `7909b901df4293ef…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NB ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1991-820609](https://doi.org/10.1515/ijmr-1991-820609) A. Fernandez Guillermet, Z. Metallkd., 82, 478-87(1991).  
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
