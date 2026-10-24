# Co–Cu phases

> Co–Cu system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-CU.html · Markdown: https://data.orchid-project.org/phases/pages/CO-CU.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-CU) · [full JSON](https://data.orchid-project.org/phases/systems/CO-CU.json) · [Co–Cu system page](https://data.orchid-project.org/systems/CO-CU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-CU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Cu system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-cu-bcc-a2); _phase:co-cu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-co-cu-fcc-a1); _phase:co-cu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1877.99 K, x(Cu) 0–1 | 11 | 4 |
| [HCP_A3](#phase-co-cu-hcp-a3); _phase:co-cu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1359.98 K, x(Cu) 0–0.00404 | 0 | 4 |
| [LIQUID](#phase-co-cu-liquid); _phase:co-cu:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 300.27–2500 K, x(Cu) 0–1 | 59 | 4 |

## BCC_A2 (Co–Cu)

- Id: `phase:co-cu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-cu:bcc-a2)

Names (5): _corpus: _corpus:phase:co-cu:bcc-a2  
_tdb: _tdb:CoCu-00Kub-LB.tdb:BCC_A2, tdb:CoCu-06Pal.tdb:BCC_A2, tdb:CoCu-80Has.tdb:BCC_A2, tdb:CoCu-97Oht.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[CoCu-00Kub-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-00Kub-LB.tdb): BCC_A2, type code %B, sha256 `e190588a17897dcb…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CO CU : VA : !
~~~~

[CoCu-06Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-06Pal.tdb): BCC_A2, type code %B, sha256 `e6f9f7cd2524034b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CO CU : VA : !
~~~~

[CoCu-80Has.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-80Has.tdb): BCC_A2, type code %B, sha256 `aab8a56c0d106053…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO CU : VA : !
~~~~

[CoCu-97Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-97Oht.tdb): BCC_A2, type code %B, sha256 `dadbec645d9a2e07…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CO CU : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(80)90026-7](https://doi.org/10.1016/0364-5916%2880%2990026-7) Mitsuhiro Hasebe, Taiji Nishizawa, Calculation of phase diagrams of the iron-copper and cobalt-copper systems, Calphad 4, 83-100 (1980).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.10.007](https://doi.org/10.1016/j.calphad.2005.10.007) Mauro Palumbo, Stefano Curiotto, Livio Battezzati, Thermodynamic analysis of the stable and metastable Co–Cu and Co–Cu–Fe phase diagrams, Calphad 30, 171-178 (2006).  
_assessment that models this phase_
- [doi:10.1361/105497100770340165](https://doi.org/10.1361/105497100770340165) Jaroslav Kubišta, Jan Vřešt’ál, Thermodynamics of the liquid Co-Cu system and calculation of phase diagram, JPE 21, 125-129 (2000).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.37.207](https://doi.org/10.2355/isijinternational.37.207) Hiroshi Ohtani, Hisashi Suda, Kiyohito Ishida, Effects of Cu and Other Tramp Elements on Steel Properties. Solid/Liquid Equilibria in Fe-Cu Based Ternary Systems., ISIJ International 37, 207-216 (1997).  
_assessment that models this phase_

## FCC_A1 (Co–Cu)

- Id: `phase:co-cu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1877.99 K, x(Cu) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-cu:fcc-a1)

Names (8): _corpus: _corpus:phase:co-cu:fcc-a1  
_paper: _paper:10.1007/s11106-007-0013-9:(Cu), paper:10.1007/s11106-007-0013-9:(αCo), paper:10.1007/s11106-007-0013-9:(αCu)  
_tdb: _tdb:CoCu-00Kub-LB.tdb:FCC_A1, tdb:CoCu-06Pal.tdb:FCC_A1, tdb:CoCu-80Has.tdb:FCC_A1, tdb:CoCu-97Oht.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CoCu-00Kub-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-00Kub-LB.tdb): FCC_A1, type code %A, sha256 `e190588a17897dcb…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CO% CU% : VA : !
~~~~

[CoCu-06Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-06Pal.tdb): FCC_A1, type code %A, sha256 `e6f9f7cd2524034b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CO% CU% : VA : !
~~~~

[CoCu-80Has.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-80Has.tdb): FCC_A1, type code %A, sha256 `aab8a56c0d106053…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% CU% : VA : !
~~~~

[CoCu-97Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-97Oht.tdb): FCC_A1, type code %A, sha256 `dadbec645d9a2e07…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CO% CU% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/0364-5916(80)90026-7](https://doi.org/10.1016/0364-5916%2880%2990026-7) Mitsuhiro Hasebe, Taiji Nishizawa, Calculation of phase diagrams of the iron-copper and cobalt-copper systems, Calphad 4, 83-100 (1980).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.10.007](https://doi.org/10.1016/j.calphad.2005.10.007) Mauro Palumbo, Stefano Curiotto, Livio Battezzati, Thermodynamic analysis of the stable and metastable Co–Cu and Co–Cu–Fe phase diagrams, Calphad 30, 171-178 (2006).  
_assessment that models this phase_
- [doi:10.1361/105497100770340165](https://doi.org/10.1361/105497100770340165) Jaroslav Kubišta, Jan Vřešt’ál, Thermodynamics of the liquid Co-Cu system and calculation of phase diagram, JPE 21, 125-129 (2000).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.37.207](https://doi.org/10.2355/isijinternational.37.207) Hiroshi Ohtani, Hisashi Suda, Kiyohito Ishida, Effects of Cu and Other Tramp Elements on Steel Properties. Solid/Liquid Equilibria in Fe-Cu Based Ternary Systems., ISIJ International 37, 207-216 (1997).  
_assessment that models this phase_
- [doi:10.1007/s11106-007-0013-9](https://doi.org/10.1007/s11106-007-0013-9) M. A. Turchanin, P. G. Agraval, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. V. Copper-cobalt system, Powder Metall Met Ceram 46, 77-89 (2007).  
_reports values for this phase_

## HCP_A3 (Co–Cu)

- Id: `phase:co-cu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1359.98 K, x(Cu) 0–0.00404
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-cu:hcp-a3)

Names (5): _corpus: _corpus:phase:co-cu:hcp-a3  
_tdb: _tdb:CoCu-00Kub-LB.tdb:HCP_A3, tdb:CoCu-06Pal.tdb:HCP_A3, tdb:CoCu-80Has.tdb:HCP_A3, tdb:CoCu-97Oht.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CoCu-00Kub-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-00Kub-LB.tdb): HCP_A3, type code %A, sha256 `e190588a17897dcb…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CO% CU : VA : !
~~~~

[CoCu-06Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-06Pal.tdb): HCP_A3, type code %A, sha256 `e6f9f7cd2524034b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CO% CU : VA : !
~~~~

[CoCu-80Has.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-80Has.tdb): HCP_A3, type code %A, sha256 `aab8a56c0d106053…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% CU : VA : !
~~~~

[CoCu-97Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-97Oht.tdb): HCP_A3, type code %A, sha256 `dadbec645d9a2e07…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CO% CU : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(80)90026-7](https://doi.org/10.1016/0364-5916%2880%2990026-7) Mitsuhiro Hasebe, Taiji Nishizawa, Calculation of phase diagrams of the iron-copper and cobalt-copper systems, Calphad 4, 83-100 (1980).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.10.007](https://doi.org/10.1016/j.calphad.2005.10.007) Mauro Palumbo, Stefano Curiotto, Livio Battezzati, Thermodynamic analysis of the stable and metastable Co–Cu and Co–Cu–Fe phase diagrams, Calphad 30, 171-178 (2006).  
_assessment that models this phase_
- [doi:10.1361/105497100770340165](https://doi.org/10.1361/105497100770340165) Jaroslav Kubišta, Jan Vřešt’ál, Thermodynamics of the liquid Co-Cu system and calculation of phase diagram, JPE 21, 125-129 (2000).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.37.207](https://doi.org/10.2355/isijinternational.37.207) Hiroshi Ohtani, Hisashi Suda, Kiyohito Ishida, Effects of Cu and Other Tramp Elements on Steel Properties. Solid/Liquid Equilibria in Fe-Cu Based Ternary Systems., ISIJ International 37, 207-216 (1997).  
_assessment that models this phase_

## LIQUID (Co–Cu)

- Id: `phase:co-cu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300.27–2500 K, x(Cu) 0–1
- Literature: 59 values (59 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-cu:liquid)

Names (7): _corpus: _corpus:phase:co-cu:liquid  
_paper: _paper:10.1007/s11106-007-0013-9:L, paper:10.1361/105497100770340165:liquid  
_tdb: _tdb:CoCu-00Kub-LB.tdb:LIQUID, tdb:CoCu-06Pal.tdb:LIQUID, tdb:CoCu-80Has.tdb:LIQUID, tdb:CoCu-97Oht.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CoCu-00Kub-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-00Kub-LB.tdb): LIQUID, type code %, sha256 `e190588a17897dcb…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CO CU : !
~~~~

[CoCu-06Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-06Pal.tdb): LIQUID, type code %, sha256 `e6f9f7cd2524034b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CO CU : !
~~~~

[CoCu-80Has.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-80Has.tdb): LIQUID, type code %, sha256 `aab8a56c0d106053…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO CU : !
~~~~

[CoCu-97Oht.tdb](https://orchid-project.org/data/databases/sgte-binary/CoCu-97Oht.tdb): LIQUID, type code %, sha256 `dadbec645d9a2e07…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CO CU : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497100770340165](https://doi.org/10.1361/105497100770340165) Jaroslav Kubišta, Jan Vřešt’ál, Thermodynamics of the liquid Co-Cu system and calculation of phase diagram, JPE 21, 125-129 (2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(80)90026-7](https://doi.org/10.1016/0364-5916%2880%2990026-7) Mitsuhiro Hasebe, Taiji Nishizawa, Calculation of phase diagrams of the iron-copper and cobalt-copper systems, Calphad 4, 83-100 (1980).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2005.10.007](https://doi.org/10.1016/j.calphad.2005.10.007) Mauro Palumbo, Stefano Curiotto, Livio Battezzati, Thermodynamic analysis of the stable and metastable Co–Cu and Co–Cu–Fe phase diagrams, Calphad 30, 171-178 (2006).  
_assessment that models this phase_
- [doi:10.2355/isijinternational.37.207](https://doi.org/10.2355/isijinternational.37.207) Hiroshi Ohtani, Hisashi Suda, Kiyohito Ishida, Effects of Cu and Other Tramp Elements on Steel Properties. Solid/Liquid Equilibria in Fe-Cu Based Ternary Systems., ISIJ International 37, 207-216 (1997).  
_assessment that models this phase_
- [doi:10.1007/s11106-007-0013-9](https://doi.org/10.1007/s11106-007-0013-9) M. A. Turchanin, P. G. Agraval, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. V. Copper-cobalt system, Powder Metall Met Ceram 46, 77-89 (2007).  
_reports values for this phase_

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
