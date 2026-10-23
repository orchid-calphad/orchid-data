# Nb–W phases

> Nb–W system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-W.html · Markdown: https://data.orchid-project.org/phases/pages/NB-W.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-W) · [full JSON](https://data.orchid-project.org/phases/systems/NB-W.json) · [Nb–W system page](https://data.orchid-project.org/systems/NB-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–W system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nb-w-bcc-a2); _phase:nb-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 3 calculated diagram(s): 300–3999.9 K, x(W) 0–1 | 0 | 3 |
| [B2_BCC](#phase-nb-w-bcc-b2); _phase:nb-w:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3210 K, x(W) 0.4–0.57 | 0 | 1 |
| [FCC_A1](#phase-nb-w-fcc-a1); _phase:nb-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-nb-w-hcp-a3); _phase:nb-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-nb-w-liquid); _phase:nb-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2713–4000 K, x(W) 0–1 | 0 | 2 |

## BCC_A2 (Nb–W)

- Id: `phase:nb-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 3 calculated diagram(s): 300–3999.9 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-w:bcc-a2)

Names (4): _corpus: _corpus:phase:nb-w:bcc-a2  
_tdb: _tdb:NbW-22Zha.tdb:A2_BCC, tdb:NbW-22Zha.tdb:BCC_A2, tdb:NbW-97Hua-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[NbW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-22Zha.tdb): A2_BCC, type code %B, sha256 `7dd5513e71703152…`

~~~~text
44: PHASE A2_BCC %B 2 1 3 !
45: CONST A2_BCC : NB W : VA : !
~~~~

[NbW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-22Zha.tdb): BCC_A2, type code %B, sha256 `7dd5513e71703152…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : NB% W% : VA : !
~~~~

[NbW-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-97Hua-LB.tdb): BCC_A2, type code %B, sha256 `372bf17dac293b84…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NB% W% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

## B2_BCC (Nb–W)

- Id: `phase:nb-w:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: NbW-22Zha.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in NbW-22Zha.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–3210 K, x(W) 0.4–0.57
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-w:bcc-b2)

Names (2): _corpus: _corpus:phase:nb-w:bcc-b2  
_tdb: _tdb:NbW-22Zha.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[NbW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-22Zha.tdb): B2_BCC, type code %BO, sha256 `7dd5513e71703152…`

~~~~text
49: PHASE B2_BCC %BO 3 0.5 0.5 3 !
50: CONST B2_BCC : NB W : NB W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_

## FCC_A1 (Nb–W)

- Id: `phase:nb-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-w:fcc-a1)

Names (3): _corpus: _corpus:phase:nb-w:fcc-a1  
_tdb: _tdb:NbW-22Zha.tdb:FCC_A1, tdb:NbW-97Hua-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NbW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-22Zha.tdb): FCC_A1, type code %A, sha256 `7dd5513e71703152…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : NB W : VA : !
~~~~

[NbW-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-97Hua-LB.tdb): FCC_A1, type code %A, sha256 `372bf17dac293b84…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NB W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

## HCP_A3 (Nb–W)

- Id: `phase:nb-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-w:hcp-a3)

Names (3): _corpus: _corpus:phase:nb-w:hcp-a3  
_tdb: _tdb:NbW-22Zha.tdb:HCP_A3, tdb:NbW-97Hua-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NbW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-22Zha.tdb): HCP_A3, type code %A, sha256 `7dd5513e71703152…`

~~~~text
54: PHASE HCP_A3 %A 2 1 0.5 !
55: CONST HCP_A3 : NB W : VA : !
~~~~

[NbW-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-97Hua-LB.tdb): HCP_A3, type code %A, sha256 `372bf17dac293b84…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NB W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
_assessment that models this phase_

## LIQUID (Nb–W)

- Id: `phase:nb-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2713–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-w:liquid)

Names (3): _corpus: _corpus:phase:nb-w:liquid  
_tdb: _tdb:NbW-22Zha.tdb:LIQUID, tdb:NbW-97Hua-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NbW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-22Zha.tdb): LIQUID, type code %, sha256 `7dd5513e71703152…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : NB W : !
~~~~

[NbW-97Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbW-97Hua-LB.tdb): LIQUID, type code %, sha256 `372bf17dac293b84…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NB W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0010](https://doi.org/10.3139/ijmr-1997-0010) W. Huang, M. Selleby, Z. Metallkd., 88, 55-62(1997).  
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
