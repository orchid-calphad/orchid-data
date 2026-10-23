# Si–Zn phases

> Si–Zn system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SI-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/SI-ZN.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SI-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/SI-ZN.json) · [Si–Zn system page](https://data.orchid-project.org/systems/SI-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SI-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Si–Zn system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-si-zn-a4-diamond); _phase:si-zn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Zn) 0–0 | 3 | 3 |
| [BCC_A2](#phase-si-zn-bcc-a2); _phase:si-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-si-zn-fcc-a1); _phase:si-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-si-zn-hcp-a3); _phase:si-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.92 K, x(Zn) 1–1 | 1 | 3 |
| [LIQUID](#phase-si-zn-liquid); _phase:si-zn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 692.17–2500 K, x(Zn) 0–1 | 3 | 3 |

## DIAMOND_A4 (Si–Zn)

- Id: `phase:si-zn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Zn) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-zn:a4-diamond)

Names (5): _corpus: _corpus:phase:si-zn:a4-diamond  
_paper: _paper:10.1016/s0364-5916(96)00033-8:\<Si>  
_tdb: _tdb:SiZn-24Zob-3g.tdb:DIAMOND_A4, tdb:SiZn-86Mey.tdb:DIAMOND_A4, tdb:SiZn-96Jac-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[SiZn-24Zob-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-24Zob-3g.tdb): DIAMOND_A4, type code %, sha256 `cb2045515769b6f8…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

[SiZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-86Mey.tdb): DIAMOND_A4, type code %, sha256 `a01184415c4bd4f9…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SI% ZN : !
~~~~

[SiZn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-96Jac-LB.tdb): DIAMOND_A4, type code %, sha256 `56568b4c0531129d…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SI% ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102742](https://doi.org/10.1016/j.calphad.2024.102742) O. Zobac, A. Kroupa, A. Dinsdale, Calphad, 87, 102742(2024).  
_assessment that models this phase_

## BCC_A2 (Si–Zn)

- Id: `phase:si-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-zn:bcc-a2)

Names (3): _corpus: _corpus:phase:si-zn:bcc-a2  
_tdb: _tdb:SiZn-86Mey.tdb:BCC_A2, tdb:SiZn-96Jac-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[SiZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-86Mey.tdb): BCC_A2, type code %B, sha256 `a01184415c4bd4f9…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SI ZN : VA : !
~~~~

[SiZn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-96Jac-LB.tdb): BCC_A2, type code %B, sha256 `56568b4c0531129d…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SI ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase_

## FCC_A1 (Si–Zn)

- Id: `phase:si-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-zn:fcc-a1)

Names (4): _corpus: _corpus:phase:si-zn:fcc-a1  
_tdb: _tdb:SiZn-24Zob-3g.tdb:FCC_A1, tdb:SiZn-86Mey.tdb:FCC_A1, tdb:SiZn-96Jac-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[SiZn-24Zob-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-24Zob-3g.tdb): FCC_A1, type code %A, sha256 `cb2045515769b6f8…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : SI ZN : VA : !
~~~~

[SiZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-86Mey.tdb): FCC_A1, type code %A, sha256 `a01184415c4bd4f9…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SI ZN : VA : !
~~~~

[SiZn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-96Jac-LB.tdb): FCC_A1, type code %A, sha256 `56568b4c0531129d…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SI ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2024.102742](https://doi.org/10.1016/j.calphad.2024.102742) O. Zobac, A. Kroupa, A. Dinsdale, Calphad, 87, 102742(2024).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase_

## HCP_A3 (Si–Zn)

- Id: `phase:si-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.92 K, x(Zn) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-zn:hcp-a3)

Names (5): _corpus: _corpus:phase:si-zn:hcp-a3  
_paper: _paper:10.1016/s0364-5916(96)00033-8:\<Zn>  
_tdb: _tdb:SiZn-24Zob-3g.tdb:HCP_A3, tdb:SiZn-86Mey.tdb:HCP_A3, tdb:SiZn-96Jac-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[SiZn-24Zob-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-24Zob-3g.tdb): HCP_A3, type code %A, sha256 `cb2045515769b6f8…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : SI ZN% : VA : !
~~~~

[SiZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-86Mey.tdb): HCP_A3, type code %A, sha256 `a01184415c4bd4f9…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SI ZN : VA : !
~~~~

[SiZn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-96Jac-LB.tdb): HCP_A3, type code %A, sha256 `56568b4c0531129d…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : SI ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102742](https://doi.org/10.1016/j.calphad.2024.102742) O. Zobac, A. Kroupa, A. Dinsdale, Calphad, 87, 102742(2024).  
_assessment that models this phase_

## LIQUID (Si–Zn)

- Id: `phase:si-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 692.17–2500 K, x(Zn) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:si-zn:liquid)

Names (5): _corpus: _corpus:phase:si-zn:liquid  
_paper: _paper:10.1016/s0364-5916(96)00033-8:Liq  
_tdb: _tdb:SiZn-24Zob-3g.tdb:LIQUID, tdb:SiZn-86Mey.tdb:LIQUID, tdb:SiZn-96Jac-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[SiZn-24Zob-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-24Zob-3g.tdb): LIQUID, type code %, sha256 `cb2045515769b6f8…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SI ZN : !
~~~~

[SiZn-86Mey.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-86Mey.tdb): LIQUID, type code %, sha256 `a01184415c4bd4f9…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SI ZN : !
~~~~

[SiZn-96Jac-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SiZn-96Jac-LB.tdb): LIQUID, type code %, sha256 `56568b4c0531129d…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SI ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0364-5916(96)00033-8](https://doi.org/10.1016/S0364-5916%2896%2900033-8) M.H.G. Jacobs, P.J. Spencer, Calphad, 20, 307-20(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2024.102742](https://doi.org/10.1016/j.calphad.2024.102742) O. Zobac, A. Kroupa, A. Dinsdale, Calphad, 87, 102742(2024).  
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
