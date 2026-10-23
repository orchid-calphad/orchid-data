# N–Nb phases

> N–Nb system: 5 phases (tier A 3, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/N-NB.html · Markdown: https://data.orchid-project.org/phases/pages/N-NB.md

5 phases (tier A 3, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=N-NB) · [full JSON](https://data.orchid-project.org/phases/systems/N-NB.json) · [N–Nb system page](https://data.orchid-project.org/systems/N-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/N-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the N–Nb system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-n-nb-bcc-a2); _phase:n-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2767.09 K, x(N) 0–0.20934 | 0 | 3 |
| [FCC_A1](#phase-n-nb-fcc-a1); _phase:n-nb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2350 K, x(N) 0.40025–0.5 | 0 | 3 |
| [HCP_A3](#phase-n-nb-hcp-a3); _phase:n-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2858.19 K, x(N) 0.2947–0.33333 | 0 | 3 |
| [LIQUID](#phase-n-nb-liquid); _phase:n-nb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 2688.39–4000 K, x(N) 0–0.24595 | 3 | 3 |
| [N2GAS](#phase-n-nb-n2gas); _phase:n-nb:n2gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300–4000 K, x(N) 1–1 | 0 | 3 |

## BCC_A2 (N–Nb)

- Id: `phase:n-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2767.09 K, x(N) 0–0.20934
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-nb:bcc-a2)

Names (4): _corpus: _corpus:phase:n-nb:bcc-a2  
_tdb: _tdb:NbN-09Hal.tdb:BCC_A2, tdb:NbN-13Khv.tdb:BCC_A2, tdb:NbN-96Hua-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[NbN-09Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-09Hal.tdb): BCC_A2, type code %B, sha256 `bf2dd17a6932b77d…`

~~~~text
37: PHASE BCC_A2 %B 2 1 1 !
38: CONST BCC_A2 : NB% : N VA% : !
~~~~

[NbN-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-13Khv.tdb): BCC_A2, type code %B, sha256 `b1c67a6776138cb9…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NB% : N VA% : !
~~~~

[NbN-96Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-96Hua-LB.tdb): BCC_A2, type code %B, sha256 `e10e5bfc05a45030…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : NB% : N VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02595450](https://doi.org/10.1007/BF02595450) W. Huang, Metall. Mater. Trans. A, 27A, 3591-3600(1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.09.013](https://doi.org/10.1016/j.calphad.2008.09.013) Bengt Hallstedt, Dejan Djurovic, Modelling of interstitials in the bcc phase, Calphad 33, 233-236 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_

## FCC_A1 (N–Nb)

- Id: `phase:n-nb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2350 K, x(N) 0.40025–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-nb:fcc-a1)

Names (4): _corpus: _corpus:phase:n-nb:fcc-a1  
_tdb: _tdb:NbN-09Hal.tdb:FCC_A1, tdb:NbN-13Khv.tdb:FCC_A1, tdb:NbN-96Hua-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[NbN-09Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-09Hal.tdb): FCC_A1, type code %A, sha256 `bf2dd17a6932b77d…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NB : N VA% : !
~~~~

[NbN-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-13Khv.tdb): FCC_A1, type code %A, sha256 `b1c67a6776138cb9…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : NB : N VA% : !
~~~~

[NbN-96Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-96Hua-LB.tdb): FCC_A1, type code %A, sha256 `e10e5bfc05a45030…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : NB : N VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02595450](https://doi.org/10.1007/BF02595450) W. Huang, Metall. Mater. Trans. A, 27A, 3591-3600(1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.09.013](https://doi.org/10.1016/j.calphad.2008.09.013) Bengt Hallstedt, Dejan Djurovic, Modelling of interstitials in the bcc phase, Calphad 33, 233-236 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_

## HCP_A3 (N–Nb)

- Id: `phase:n-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2858.19 K, x(N) 0.2947–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-nb:hcp-a3)

Names (4): _corpus: _corpus:phase:n-nb:hcp-a3  
_tdb: _tdb:NbN-09Hal.tdb:HCP_A3, tdb:NbN-13Khv.tdb:HCP_A3, tdb:NbN-96Hua-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[NbN-09Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-09Hal.tdb): HCP_A3, type code %A, sha256 `bf2dd17a6932b77d…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : NB : N VA% : !
~~~~

[NbN-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-13Khv.tdb): HCP_A3, type code %A, sha256 `b1c67a6776138cb9…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : NB : N VA% : !
~~~~

[NbN-96Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-96Hua-LB.tdb): HCP_A3, type code %A, sha256 `e10e5bfc05a45030…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : NB : N VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02595450](https://doi.org/10.1007/BF02595450) W. Huang, Metall. Mater. Trans. A, 27A, 3591-3600(1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.09.013](https://doi.org/10.1016/j.calphad.2008.09.013) Bengt Hallstedt, Dejan Djurovic, Modelling of interstitials in the bcc phase, Calphad 33, 233-236 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_

## LIQUID (N–Nb)

- Id: `phase:n-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2688.39–4000 K, x(N) 0–0.24595
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-nb:liquid)

Names (5): _corpus: _corpus:phase:n-nb:liquid  
_paper: _paper:10.1007/bf02595450:liquid  
_tdb: _tdb:NbN-09Hal.tdb:LIQUID, tdb:NbN-13Khv.tdb:LIQUID, tdb:NbN-96Hua-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[NbN-09Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-09Hal.tdb): LIQUID, type code %, sha256 `bf2dd17a6932b77d…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : N NB : !
~~~~

[NbN-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-13Khv.tdb): LIQUID, type code %, sha256 `b1c67a6776138cb9…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : N NB : !
~~~~

[NbN-96Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-96Hua-LB.tdb): LIQUID, type code %, sha256 `e10e5bfc05a45030…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : N NB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02595450](https://doi.org/10.1007/BF02595450) W. Huang, Metall. Mater. Trans. A, 27A, 3591-3600(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.09.013](https://doi.org/10.1016/j.calphad.2008.09.013) Bengt Hallstedt, Dejan Djurovic, Modelling of interstitials in the bcc phase, Calphad 33, 233-236 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
_assessment that models this phase_
- [doi:10.1002/zaac.19251430121](https://doi.org/10.1002/zaac.19251430121) Ernst Friederich, Lieselotte Sittig, Herstellung und Eigenschaften von Nitriden, Z. Anorg. Allg. Chem. 143, 293-320 (1925).  
_cited as the source of values for this phase_

## N2GAS (N–Nb)

- Id: `phase:n-nb:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–4000 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-nb:n2gas)

Names (4): _corpus: _corpus:phase:n-nb:n2gas  
_tdb: _tdb:NbN-09Hal.tdb:N2GAS, tdb:NbN-13Khv.tdb:N2GAS, tdb:NbN-96Hua-LB.tdb:N2GAS  


### TDB models of N2GAS (3): PHASE and CONSTITUENT statements as written

[NbN-09Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-09Hal.tdb): N2GAS, type code %, sha256 `bf2dd17a6932b77d…`

~~~~text
45: PHASE N2GAS % 1 1 !
46: CONST N2GAS : N2 : !
~~~~

[NbN-13Khv.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-13Khv.tdb): N2GAS, type code %, sha256 `b1c67a6776138cb9…`

~~~~text
46: PHASE N2GAS % 1 1 !
47: CONST N2GAS : N2 : !
~~~~

[NbN-96Hua-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbN-96Hua-LB.tdb): N2GAS, type code %, sha256 `e10e5bfc05a45030…`

~~~~text
45: PHASE N2GAS % 1 1 !
46: CONST N2GAS : N2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02595450](https://doi.org/10.1007/BF02595450) W. Huang, Metall. Mater. Trans. A, 27A, 3591-3600(1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.09.013](https://doi.org/10.1016/j.calphad.2008.09.013) Bengt Hallstedt, Dejan Djurovic, Modelling of interstitials in the bcc phase, Calphad 33, 233-236 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2012.11.001](https://doi.org/10.1016/j.calphad.2012.11.001) A.V. Khvan, B. Hallstedt, Calphad, 40, 10-15(2013).  
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
