# Ta–W phases

> Ta–W system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TA-W.html · Markdown: https://data.orchid-project.org/phases/pages/TA-W.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TA-W) · [full JSON](https://data.orchid-project.org/phases/systems/TA-W.json) · [Ta–W system page](https://data.orchid-project.org/systems/TA-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/TA-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ta–W system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ta-w-bcc-a2); _phase:ta-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–3999.9 K, x(W) 0–1 | 0 | 6 |
| [B2_BCC](#phase-ta-w-bcc-b2); _phase:ta-w:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3690 K, x(W) 0.16–0.97 | 0 | 2 |
| [FCC_A1](#phase-ta-w-fcc-a1); _phase:ta-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-ta-w-hcp-a3); _phase:ta-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-ta-w-liquid); _phase:ta-w:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 3287–4000 K, x(W) 0–1 | 0 | 4 |

## BCC_A2 (Ta–W)

- Id: `phase:ta-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–3999.9 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-w:bcc-a2)

Names (7): _corpus: _corpus:phase:ta-w:bcc-a2  
_tdb: _tdb:TaW-01Kau-LB.tdb:A2_BCC, tdb:TaW-01Kau-LB.tdb:BCC_A2, tdb:TaW-14Guo.tdb:BCC_A2, tdb:TaW-22Zha.tdb:A2_BCC, tdb:TaW-22Zha.tdb:BCC_A2, tdb:TaW-95Fer.tdb:BCC_A2  


### TDB models of BCC_A2 (6): PHASE and CONSTITUENT statements as written

[TaW-01Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-01Kau-LB.tdb): A2_BCC, type code %B, sha256 `06799384d8b11b4b…`

~~~~text
45: PHASE A2_BCC %B 2 1 3 !
46: CONST A2_BCC : TA W : VA : !
~~~~

[TaW-01Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-01Kau-LB.tdb): BCC_A2, type code %B, sha256 `06799384d8b11b4b…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : TA% W% : VA : !
~~~~

[TaW-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-14Guo.tdb): BCC_A2, type code %B, sha256 `e48b844bab28b6a1…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : TA% W% : VA : !
~~~~

[TaW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-22Zha.tdb): A2_BCC, type code %B, sha256 `3daec7c0661909a7…`

~~~~text
42: PHASE A2_BCC %B 2 1 3 !
43: CONST A2_BCC : TA W : VA : !
~~~~

[TaW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-22Zha.tdb): BCC_A2, type code %B, sha256 `3daec7c0661909a7…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : TA% W% : VA : !
~~~~

[TaW-95Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-95Fer.tdb): BCC_A2, type code %B, sha256 `50f38ebf2b2eefbf…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : TA% W% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00061-X](https://doi.org/10.1016/S0364-5916%2801%2900061-X) L. Kaufman, P.E.A. Turchi, W. Huang, Z.-K. Liu, Calphad, 25, 419-33(2001).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
_assessment that models this phase_

## B2_BCC (Ta–W)

- Id: `phase:ta-w:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: TaW-01Kau-LB.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: TaW-22Zha.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in TaW-01Kau-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in TaW-22Zha.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–3690 K, x(W) 0.16–0.97
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-w:bcc-b2)

Names (3): _corpus: _corpus:phase:ta-w:bcc-b2  
_tdb: _tdb:TaW-01Kau-LB.tdb:B2_BCC, tdb:TaW-22Zha.tdb:B2_BCC  


### TDB models of B2_BCC (2): PHASE and CONSTITUENT statements as written

[TaW-01Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-01Kau-LB.tdb): B2_BCC, type code %BO, sha256 `06799384d8b11b4b…`

~~~~text
50: PHASE B2_BCC %BO 3 0.5 0.5 3 !
51: CONST B2_BCC : TA W : TA W : VA : !
~~~~

[TaW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-22Zha.tdb): B2_BCC, type code %BO, sha256 `3daec7c0661909a7…`

~~~~text
47: PHASE B2_BCC %BO 3 0.5 0.5 3 !
48: CONST B2_BCC : TA W : TA W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00061-X](https://doi.org/10.1016/S0364-5916%2801%2900061-X) L. Kaufman, P.E.A. Turchi, W. Huang, Z.-K. Liu, Calphad, 25, 419-33(2001).  
_assessment that models this phase_

## FCC_A1 (Ta–W)

- Id: `phase:ta-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-w:fcc-a1)

Names (5): _corpus: _corpus:phase:ta-w:fcc-a1  
_tdb: _tdb:TaW-01Kau-LB.tdb:FCC_A1, tdb:TaW-14Guo.tdb:FCC_A1, tdb:TaW-22Zha.tdb:FCC_A1, tdb:TaW-95Fer.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[TaW-01Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-01Kau-LB.tdb): FCC_A1, type code %A, sha256 `06799384d8b11b4b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : TA W : VA : !
~~~~

[TaW-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-14Guo.tdb): FCC_A1, type code %A, sha256 `e48b844bab28b6a1…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : TA W : VA : !
~~~~

[TaW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-22Zha.tdb): FCC_A1, type code %A, sha256 `3daec7c0661909a7…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : TA W : VA : !
~~~~

[TaW-95Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-95Fer.tdb): FCC_A1, type code %A, sha256 `50f38ebf2b2eefbf…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : TA W : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00061-X](https://doi.org/10.1016/S0364-5916%2801%2900061-X) L. Kaufman, P.E.A. Turchi, W. Huang, Z.-K. Liu, Calphad, 25, 419-33(2001).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
_assessment that models this phase_

## HCP_A3 (Ta–W)

- Id: `phase:ta-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-w:hcp-a3)

Names (5): _corpus: _corpus:phase:ta-w:hcp-a3  
_tdb: _tdb:TaW-01Kau-LB.tdb:HCP_A3, tdb:TaW-14Guo.tdb:HCP_A3, tdb:TaW-22Zha.tdb:HCP_A3, tdb:TaW-95Fer.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[TaW-01Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-01Kau-LB.tdb): HCP_A3, type code %A, sha256 `06799384d8b11b4b…`

~~~~text
55: PHASE HCP_A3 %A 2 1 0.5 !
56: CONST HCP_A3 : TA W : VA : !
~~~~

[TaW-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-14Guo.tdb): HCP_A3, type code %A, sha256 `e48b844bab28b6a1…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : TA W : VA : !
~~~~

[TaW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-22Zha.tdb): HCP_A3, type code %A, sha256 `3daec7c0661909a7…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : TA W : VA : !
~~~~

[TaW-95Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-95Fer.tdb): HCP_A3, type code %A, sha256 `50f38ebf2b2eefbf…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : TA W : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00061-X](https://doi.org/10.1016/S0364-5916%2801%2900061-X) L. Kaufman, P.E.A. Turchi, W. Huang, Z.-K. Liu, Calphad, 25, 419-33(2001).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
_assessment that models this phase_

## LIQUID (Ta–W)

- Id: `phase:ta-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 3287–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ta-w:liquid)

Names (5): _corpus: _corpus:phase:ta-w:liquid  
_tdb: _tdb:TaW-01Kau-LB.tdb:LIQUID, tdb:TaW-14Guo.tdb:LIQUID, tdb:TaW-22Zha.tdb:LIQUID, tdb:TaW-95Fer.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[TaW-01Kau-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-01Kau-LB.tdb): LIQUID, type code %, sha256 `06799384d8b11b4b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : TA W : !
~~~~

[TaW-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-14Guo.tdb): LIQUID, type code %, sha256 `e48b844bab28b6a1…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : TA W : !
~~~~

[TaW-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-22Zha.tdb): LIQUID, type code %, sha256 `3daec7c0661909a7…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : TA W : !
~~~~

[TaW-95Fer.tdb](https://orchid-project.org/data/databases/sgte-binary/TaW-95Fer.tdb): LIQUID, type code %, sha256 `50f38ebf2b2eefbf…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : TA W : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00061-X](https://doi.org/10.1016/S0364-5916%2801%2900061-X) L. Kaufman, P.E.A. Turchi, W. Huang, Z.-K. Liu, Calphad, 25, 419-33(2001).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
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
