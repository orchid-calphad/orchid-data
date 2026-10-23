# Au–Si phases

> Au–Si system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-SI.html · Markdown: https://data.orchid-project.org/phases/pages/AU-SI.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-SI) · [full JSON](https://data.orchid-project.org/phases/systems/AU-SI.json) · [Au–Si system page](https://data.orchid-project.org/systems/AU-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Si system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-au-si-a4-diamond); _phase:au-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2499.87 K, x(Si) 0.99994–1 | 0 | 4 |
| [BCC_A2](#phase-au-si-bcc-a2); _phase:au-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-au-si-fcc-a1); _phase:au-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1356.68 K, x(Si) 0–0.00085 | 0 | 4 |
| [HCP_A3](#phase-au-si-hcp-a3); _phase:au-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-au-si-liquid); _phase:au-si:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 632.53–2500 K, x(Si) 0–1 | 0 | 4 |

## DIAMOND_A4 (Au–Si)

- Id: `phase:au-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2499.87 K, x(Si) 0.99994–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-si:a4-diamond)

Names (5): _corpus: _corpus:phase:au-si:a4-diamond  
_tdb: _tdb:AuSi-07Men.tdb:DIAMOND_A4, tdb:AuSi-85Sau.tdb:DIAMOND_A4, tdb:AuSi-89Che.tdb:DIAMOND_A4, tdb:AuSi-98Che-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[AuSi-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-07Men.tdb): DIAMOND_A4, type code %, sha256 `fb773e4798f0139d…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : AU SI% : !
~~~~

[AuSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-85Sau.tdb): DIAMOND_A4, type code %, sha256 `af731068b76937fd…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : SI : !
~~~~

[AuSi-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-89Che.tdb): DIAMOND_A4, type code %, sha256 `0215614f9582b192…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : AU SI% : !
~~~~

[AuSi-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-98Che-LB.tdb): DIAMOND_A4, type code %, sha256 `5a11525d97fbc6bb…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## BCC_A2 (Au–Si)

- Id: `phase:au-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-si:bcc-a2)

Names (5): _corpus: _corpus:phase:au-si:bcc-a2  
_tdb: _tdb:AuSi-07Men.tdb:BCC_A2, tdb:AuSi-85Sau.tdb:BCC_A2, tdb:AuSi-89Che.tdb:BCC_A2, tdb:AuSi-98Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[AuSi-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-07Men.tdb): BCC_A2, type code %B, sha256 `fb773e4798f0139d…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : AU SI : VA : !
~~~~

[AuSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-85Sau.tdb): BCC_A2, type code %B, sha256 `af731068b76937fd…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : AU SI : VA : !
~~~~

[AuSi-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-89Che.tdb): BCC_A2, type code %B, sha256 `0215614f9582b192…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU SI : VA : !
~~~~

[AuSi-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-98Che-LB.tdb): BCC_A2, type code %B, sha256 `5a11525d97fbc6bb…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AU SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## FCC_A1 (Au–Si)

- Id: `phase:au-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1356.68 K, x(Si) 0–0.00085
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-si:fcc-a1)

Names (5): _corpus: _corpus:phase:au-si:fcc-a1  
_tdb: _tdb:AuSi-07Men.tdb:FCC_A1, tdb:AuSi-85Sau.tdb:FCC_A1, tdb:AuSi-89Che.tdb:FCC_A1, tdb:AuSi-98Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[AuSi-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-07Men.tdb): FCC_A1, type code %A, sha256 `fb773e4798f0139d…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : AU% SI : VA : !
~~~~

[AuSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-85Sau.tdb): FCC_A1, type code %A, sha256 `af731068b76937fd…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : AU% SI : VA : !
~~~~

[AuSi-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-89Che.tdb): FCC_A1, type code %A, sha256 `0215614f9582b192…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU% SI : VA : !
~~~~

[AuSi-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-98Che-LB.tdb): FCC_A1, type code %A, sha256 `5a11525d97fbc6bb…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AU% SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## HCP_A3 (Au–Si)

- Id: `phase:au-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-si:hcp-a3)

Names (5): _corpus: _corpus:phase:au-si:hcp-a3  
_tdb: _tdb:AuSi-07Men.tdb:HCP_A3, tdb:AuSi-85Sau.tdb:HCP_A3, tdb:AuSi-89Che.tdb:HCP_A3, tdb:AuSi-98Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[AuSi-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-07Men.tdb): HCP_A3, type code %A, sha256 `fb773e4798f0139d…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : AU SI : VA : !
~~~~

[AuSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-85Sau.tdb): HCP_A3, type code %A, sha256 `af731068b76937fd…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : AU SI : VA : !
~~~~

[AuSi-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-89Che.tdb): HCP_A3, type code %A, sha256 `0215614f9582b192…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU SI : VA : !
~~~~

[AuSi-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-98Che-LB.tdb): HCP_A3, type code %A, sha256 `5a11525d97fbc6bb…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AU SI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
_assessment that models this phase_

## LIQUID (Au–Si)

- Id: `phase:au-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 632.53–2500 K, x(Si) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-si:liquid)

Names (5): _corpus: _corpus:phase:au-si:liquid  
_tdb: _tdb:AuSi-07Men.tdb:LIQUID, tdb:AuSi-85Sau.tdb:LIQUID, tdb:AuSi-89Che.tdb:LIQUID, tdb:AuSi-98Che-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[AuSi-07Men.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-07Men.tdb): LIQUID, type code %, sha256 `fb773e4798f0139d…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : AU SI : !
~~~~

[AuSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-85Sau.tdb): LIQUID, type code %, sha256 `af731068b76937fd…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : AU SI : !
~~~~

[AuSi-89Che.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-89Che.tdb): LIQUID, type code %, sha256 `0215614f9582b192…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU SI : !
~~~~

[AuSi-98Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSi-98Che-LB.tdb): LIQUID, type code %, sha256 `5a11525d97fbc6bb…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AU SI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2006.05.066](https://doi.org/10.1016/j.jallcom.2006.05.066) F.G. Meng, H.S. Liu, L.B. Liu, Z.P. Jin, Thermodynamic description of the Au–Si–Sn system, Journal of Alloys and Compounds 431, 292-297 (2007).  
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
