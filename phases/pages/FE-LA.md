# Fe–La phases

> Fe–La system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-LA.html · Markdown: https://data.orchid-project.org/phases/pages/FE-LA.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-LA) · [full JSON](https://data.orchid-project.org/phases/systems/FE-LA.json) · [Fe–La system page](https://data.orchid-project.org/systems/FE-LA.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–La system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-la-bcc-a2); _phase:fe-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.4 K, x(La) 0–1 | 0 | 2 |
| [DHCP](#phase-fe-la-dhcp-a3); _phase:fe-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1124.99 K, x(La) 1–1 | 0 | 2 |
| [FCC_A1](#phase-fe-la-fcc-a1); _phase:fe-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 549.89–1670.01 K, x(La) 0–1 | 0 | 2 |
| [HCP_A3](#phase-fe-la-hcp-a3); _phase:fe-la:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-fe-la-liquid); _phase:fe-la:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1070–2500 K, x(La) 0–1 | 0 | 2 |

## BCC_A2 (Fe–La)

- Id: `phase:fe-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.4 K, x(La) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-la:bcc-a2)

Names (3): _corpus: _corpus:phase:fe-la:bcc-a2  
_tdb: _tdb:FeLa-09Pov.tdb:BCC_A2, tdb:FeLa-23Su.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FeLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-09Pov.tdb): BCC_A2, type code %B, sha256 `93c713b8df680ffc…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : FE LA : VA : !
~~~~

[FeLa-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-23Su.tdb): BCC_A2, type code %B, sha256 `825f2df5101d7cd0…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : FE LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## DHCP (Fe–La)

- Id: `phase:fe-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1124.99 K, x(La) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-la:dhcp-a3)

Names (3): _corpus: _corpus:phase:fe-la:dhcp-a3  
_tdb: _tdb:FeLa-09Pov.tdb:DHCP, tdb:FeLa-23Su.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[FeLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-09Pov.tdb): DHCP, type code %, sha256 `93c713b8df680ffc…`

~~~~text
45: PHASE DHCP % 2 1 0.5 !
46: CONST DHCP : LA : VA : !
~~~~

[FeLa-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-23Su.tdb): DHCP, type code %, sha256 `825f2df5101d7cd0…`

~~~~text
40: PHASE DHCP % 2 1 0.5 !
41: CONST DHCP : LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## FCC_A1 (Fe–La)

- Id: `phase:fe-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 549.89–1670.01 K, x(La) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-la:fcc-a1)

Names (3): _corpus: _corpus:phase:fe-la:fcc-a1  
_tdb: _tdb:FeLa-09Pov.tdb:FCC_A1, tdb:FeLa-23Su.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FeLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-09Pov.tdb): FCC_A1, type code %A, sha256 `93c713b8df680ffc…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : FE LA : VA : !
~~~~

[FeLa-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-23Su.tdb): FCC_A1, type code %A, sha256 `825f2df5101d7cd0…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : FE LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## HCP_A3 (Fe–La)

- Id: `phase:fe-la:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Fe 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-la:hcp-a3)

Names (3): _corpus: _corpus:phase:fe-la:hcp-a3  
_tdb: _tdb:FeLa-09Pov.tdb:HCP_A3, tdb:FeLa-23Su.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FeLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-09Pov.tdb): HCP_A3, type code %A, sha256 `93c713b8df680ffc…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : FE : VA : !
~~~~

[FeLa-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-23Su.tdb): HCP_A3, type code %A, sha256 `825f2df5101d7cd0…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : FE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
_assessment that models this phase_

## LIQUID (Fe–La)

- Id: `phase:fe-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1070–2500 K, x(La) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-la:liquid)

Names (3): _corpus: _corpus:phase:fe-la:liquid  
_tdb: _tdb:FeLa-09Pov.tdb:LIQUID, tdb:FeLa-23Su.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FeLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-09Pov.tdb): LIQUID, type code %, sha256 `93c713b8df680ffc…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : FE LA : !
~~~~

[FeLa-23Su.tdb](https://orchid-project.org/data/databases/sgte-binary/FeLa-23Su.tdb): LIQUID, type code %, sha256 `825f2df5101d7cd0…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : FE LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-009-9501-6](https://doi.org/10.1007/s11669-009-9501-6) E. Povoden-Karadeniz, A. N. Grundy, M. Chen, T. Ivas, L. J. Gauckler, Thermodynamic Assessment of the La-Fe-O System, J. Phase Equilib. Diffus. 30, 351-366 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102506](https://doi.org/10.1016/j.calphad.2022.102506) D. Su, K.C. Yang, M.H. Rong, P.P. Liu, Q.R. Yao, J. Wang, Q. Chen, G.H. Rao, H.Y. Zhou, Calphad, 80, 102506(2023).  
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
