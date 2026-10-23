# C–Hf phases

> C–Hf system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-HF.html · Markdown: https://data.orchid-project.org/phases/pages/C-HF.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-HF) · [full JSON](https://data.orchid-project.org/phases/systems/C-HF.json) · [C–Hf system page](https://data.orchid-project.org/systems/C-HF.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-HF.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Hf system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-hf-a4-diamond); _phase:c-hf:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 2 | 2 |
| [GRAPHITE_A9](#phase-c-hf-a9-graphite); _phase:c-hf:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 2 |
| [BCC_A2](#phase-c-hf-bcc-a2); _phase:c-hf:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 2016.13–2506.99 K, x(C) 0–0.01068 | 9 | 2 |
| [FCC_A1](#phase-c-hf-fcc-a1); _phase:c-hf:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 0.33419–0.49872 | 14 | 2 |
| [HCP_A3](#phase-c-hf-hcp-a3); _phase:c-hf:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2649.08 K, x(C) 0–0.13983 | 9 | 2 |
| [LIQUID](#phase-c-hf-liquid); _phase:c-hf:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2463.94–4000 K, x(C) 0–0.74728 | 15 | 2 |

## DIAMOND_A4 (C–Hf)

- Id: `phase:c-hf:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-hf:a4-diamond)

Names (4): _corpus: _corpus:phase:c-hf:a4-diamond  
_paper: _paper:10.1007/s11669-997-0061-3:(αHf)  
_tdb: _tdb:HfC-16Pan.tdb:DIAMOND_A4, tdb:HfC-97Bit-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[HfC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-16Pan.tdb): DIAMOND_A4, type code %, sha256 `6a221c5bb6daa283…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : C : !
~~~~

[HfC-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-97Bit-LB.tdb): DIAMOND_A4, type code %, sha256 `920403c39afc1e2c…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-997-0061-3](https://doi.org/10.1007/s11669-997-0061-3) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the binary system hafnium-carbon (Hf-C), JPE 18, 344-356 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Hf)

- Id: `phase:c-hf:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-hf:a9-graphite)

Names (3): _corpus: _corpus:phase:c-hf:a9-graphite  
_tdb: _tdb:HfC-16Pan.tdb:GRAPHITE_A9, tdb:HfC-97Bit-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (2): PHASE and CONSTITUENT statements as written

[HfC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-16Pan.tdb): GRAPHITE_A9, type code %, sha256 `6a221c5bb6daa283…`

~~~~text
46: PHASE GRAPHITE_A9 % 1 1 !
47: CONST GRAPHITE_A9 : C : !
~~~~

[HfC-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-97Bit-LB.tdb): GRAPHITE_A9, type code %, sha256 `920403c39afc1e2c…`

~~~~text
45: PHASE GRAPHITE_A9 % 1 1 !
46: CONST GRAPHITE_A9 : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-997-0061-3](https://doi.org/10.1007/s11669-997-0061-3) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the binary system hafnium-carbon (Hf-C), JPE 18, 344-356 (1997).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_

## BCC_A2 (C–Hf)

- Id: `phase:c-hf:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2016.13–2506.99 K, x(C) 0–0.01068
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-hf:bcc-a2)

Names (4): _corpus: _corpus:phase:c-hf:bcc-a2  
_paper: _paper:10.1007/s11669-997-0061-3:βHf  
_tdb: _tdb:HfC-16Pan.tdb:BCC_A2, tdb:HfC-97Bit-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-16Pan.tdb): BCC_A2, type code %B, sha256 `6a221c5bb6daa283…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : HF : C VA% : !
~~~~

[HfC-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-97Bit-LB.tdb): BCC_A2, type code %B, sha256 `920403c39afc1e2c…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : HF : C VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-997-0061-3](https://doi.org/10.1007/s11669-997-0061-3) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the binary system hafnium-carbon (Hf-C), JPE 18, 344-356 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## FCC_A1 (C–Hf)

- Id: `phase:c-hf:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(C) 0.33419–0.49872
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-hf:fcc-a1)

Names (5): _corpus: _corpus:phase:c-hf:fcc-a1  
_paper: _paper:10.1007/s11669-997-0061-3:HfC, paper:10.1007/s11669-997-0061-3:HfC1-x  
_tdb: _tdb:HfC-16Pan.tdb:FCC_A1, tdb:HfC-97Bit-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HfC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-16Pan.tdb): FCC_A1, type code %A, sha256 `6a221c5bb6daa283…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : HF : C% VA : !
~~~~

[HfC-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-97Bit-LB.tdb): FCC_A1, type code %A, sha256 `920403c39afc1e2c…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : HF : C% VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-997-0061-3](https://doi.org/10.1007/s11669-997-0061-3) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the binary system hafnium-carbon (Hf-C), JPE 18, 344-356 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_

## HCP_A3 (C–Hf)

- Id: `phase:c-hf:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2649.08 K, x(C) 0–0.13983
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-hf:hcp-a3)

Names (4): _corpus: _corpus:phase:c-hf:hcp-a3  
_paper: _paper:10.1007/s11669-997-0061-3:αHf  
_tdb: _tdb:HfC-16Pan.tdb:HCP_A3, tdb:HfC-97Bit-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HfC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-16Pan.tdb): HCP_A3, type code %A, sha256 `6a221c5bb6daa283…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : HF : C VA% : !
~~~~

[HfC-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-97Bit-LB.tdb): HCP_A3, type code %A, sha256 `920403c39afc1e2c…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : HF : C VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-997-0061-3](https://doi.org/10.1007/s11669-997-0061-3) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the binary system hafnium-carbon (Hf-C), JPE 18, 344-356 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

## LIQUID (C–Hf)

- Id: `phase:c-hf:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2463.94–4000 K, x(C) 0–0.74728
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-hf:liquid)

Names (4): _corpus: _corpus:phase:c-hf:liquid  
_paper: _paper:10.1007/s11669-997-0061-3:L  
_tdb: _tdb:HfC-16Pan.tdb:LIQUID, tdb:HfC-97Bit-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HfC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-16Pan.tdb): LIQUID, type code %, sha256 `6a221c5bb6daa283…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : C HF : !
~~~~

[HfC-97Bit-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfC-97Bit-LB.tdb): LIQUID, type code %, sha256 `920403c39afc1e2c…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : C HF : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-997-0061-3](https://doi.org/10.1007/s11669-997-0061-3) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the binary system hafnium-carbon (Hf-C), JPE 18, 344-356 (1997).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
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
