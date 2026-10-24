# Mo–Nb phases

> Mo–Nb system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-NB.html · Markdown: https://data.orchid-project.org/phases/pages/MO-NB.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-NB) · [full JSON](https://data.orchid-project.org/phases/systems/MO-NB.json) · [Mo–Nb system page](https://data.orchid-project.org/systems/MO-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Nb system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-nb-bcc-a2); _phase:mo-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2896.02 K, x(Nb) 0–1 | 0 | 5 |
| [B2_BCC](#phase-mo-nb-bcc-b2); _phase:mo-nb:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2340 K, x(Nb) 0.14–0.97 | 0 | 1 |
| [FCC_A1](#phase-mo-nb-fcc-a1); _phase:mo-nb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-mo-nb-hcp-a3); _phase:mo-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-mo-nb-liquid); _phase:mo-nb:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 2750–4000 K, x(Nb) 0–1 | 0 | 4 |

## BCC_A2 (Mo–Nb)

- Id: `phase:mo-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2896.02 K, x(Nb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-nb:bcc-a2)

Names (6): _corpus: _corpus:phase:mo-nb:bcc-a2  
_tdb: _tdb:MoNb-04Xio.tdb:BCC_A2, tdb:MoNb-20Yen.tdb:BCC_A2, tdb:MoNb-22Zha.tdb:A2_BCC, tdb:MoNb-22Zha.tdb:BCC_A2, tdb:MoNb-80Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[MoNb-04Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-04Xio.tdb): BCC_A2, type code %B, sha256 `17d4d106c595f36b…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : MO NB : VA : !
~~~~

[MoNb-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-20Yen.tdb): BCC_A2, type code %B, sha256 `71f5ebb1a4ff9fbe…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : MO NB : VA : !
~~~~

[MoNb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-22Zha.tdb): A2_BCC, type code %B, sha256 `3171cee9dd32598e…`

~~~~text
46: PHASE A2_BCC %B 2 1 3 !
47: CONST A2_BCC : MO NB : VA : !
~~~~

[MoNb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-22Zha.tdb): BCC_A2, type code %B, sha256 `3171cee9dd32598e…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : MO% NB% : VA : !
~~~~

[MoNb-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-80Che-LB.tdb): BCC_A2, type code %B, sha256 `32a73ac4a18ea2e6…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MO NB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Liu, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_

## B2_BCC (Mo–Nb)

- Id: `phase:mo-nb:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: MoNb-22Zha.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in MoNb-22Zha.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2340 K, x(Nb) 0.14–0.97
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-nb:bcc-b2)

Names (2): _corpus: _corpus:phase:mo-nb:bcc-b2  
_tdb: _tdb:MoNb-22Zha.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[MoNb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-22Zha.tdb): B2_BCC, type code %BO, sha256 `3171cee9dd32598e…`

~~~~text
51: PHASE B2_BCC %BO 3 0.5 0.5 3 !
52: CONST B2_BCC : MO NB : MO NB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_

## FCC_A1 (Mo–Nb)

- Id: `phase:mo-nb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-nb:fcc-a1)

Names (5): _corpus: _corpus:phase:mo-nb:fcc-a1  
_tdb: _tdb:MoNb-04Xio.tdb:FCC_A1, tdb:MoNb-20Yen.tdb:FCC_A1, tdb:MoNb-22Zha.tdb:FCC_A1, tdb:MoNb-80Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[MoNb-04Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-04Xio.tdb): FCC_A1, type code %A, sha256 `17d4d106c595f36b…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : MO NB : VA : !
~~~~

[MoNb-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-20Yen.tdb): FCC_A1, type code %A, sha256 `71f5ebb1a4ff9fbe…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : MO NB : VA : !
~~~~

[MoNb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-22Zha.tdb): FCC_A1, type code %A, sha256 `3171cee9dd32598e…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : MO NB : VA : !
~~~~

[MoNb-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-80Che-LB.tdb): FCC_A1, type code %A, sha256 `32a73ac4a18ea2e6…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MO NB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Liu, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_

## HCP_A3 (Mo–Nb)

- Id: `phase:mo-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-nb:hcp-a3)

Names (5): _corpus: _corpus:phase:mo-nb:hcp-a3  
_tdb: _tdb:MoNb-04Xio.tdb:HCP_A3, tdb:MoNb-20Yen.tdb:HCP_A3, tdb:MoNb-22Zha.tdb:HCP_A3, tdb:MoNb-80Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[MoNb-04Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-04Xio.tdb): HCP_A3, type code %A, sha256 `17d4d106c595f36b…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : MO NB : VA : !
~~~~

[MoNb-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-20Yen.tdb): HCP_A3, type code %A, sha256 `71f5ebb1a4ff9fbe…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : MO NB : VA : !
~~~~

[MoNb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-22Zha.tdb): HCP_A3, type code %A, sha256 `3171cee9dd32598e…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : MO NB : VA : !
~~~~

[MoNb-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-80Che-LB.tdb): HCP_A3, type code %A, sha256 `32a73ac4a18ea2e6…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MO NB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Liu, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_

## LIQUID (Mo–Nb)

- Id: `phase:mo-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 2750–4000 K, x(Nb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-nb:liquid)

Names (5): _corpus: _corpus:phase:mo-nb:liquid  
_tdb: _tdb:MoNb-04Xio.tdb:LIQUID, tdb:MoNb-20Yen.tdb:LIQUID, tdb:MoNb-22Zha.tdb:LIQUID, tdb:MoNb-80Che-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[MoNb-04Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-04Xio.tdb): LIQUID, type code %, sha256 `17d4d106c595f36b…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : MO NB : !
~~~~

[MoNb-20Yen.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-20Yen.tdb): LIQUID, type code %, sha256 `71f5ebb1a4ff9fbe…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : MO NB : !
~~~~

[MoNb-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-22Zha.tdb): LIQUID, type code %, sha256 `3171cee9dd32598e…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : MO NB : !
~~~~

[MoNb-80Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoNb-80Che-LB.tdb): LIQUID, type code %, sha256 `32a73ac4a18ea2e6…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MO NB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Liu, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101797](https://doi.org/10.1016/j.calphad.2020.101797) Shao-yu Yen, Shu-chang Wu, M. Anshar Makhraja, Kai-chi Lo, An-chou Yeh, Kyosuke Yoshimi et al., Phase equilibria and thermodynamic assessment of the Mo–Nb-Re ternary system, Calphad 70, 101797 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
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
