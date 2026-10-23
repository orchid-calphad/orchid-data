# Pb–Sn phases

> Pb–Sn system: 6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-SN.html · Markdown: https://data.orchid-project.org/phases/pages/PB-SN.md

6 phases (tier A 5, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-SN) · [full JSON](https://data.orchid-project.org/phases/systems/PB-SN.json) · [Pb–Sn system page](https://data.orchid-project.org/systems/PB-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Sn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-pb-sn-a4-diamond); _phase:pb-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 3 calculated diagram(s): 300–300 K | 0 | 3 |
| [BCT_A5](#phase-pb-sn-a5-bct); _phase:pb-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 0.97537–1 | 0 | 3 |
| [BCC_A2](#phase-pb-sn-bcc-a2); _phase:pb-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-pb-sn-fcc-a1); _phase:pb-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–600.61 K, x(Sn) 0–0.30618 | 0 | 3 |
| [HCP_A3](#phase-pb-sn-hcp-a3); _phase:pb-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-pb-sn-liquid); _phase:pb-sn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 455.69–2500 K, x(Sn) 0–1 | 0 | 3 |

## DIAMOND_A4 (Pb–Sn)

- Id: `phase:pb-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 1 of 3 calculated diagram(s): 300–300 K
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sn:a4-diamond)

Names (4): _corpus: _corpus:phase:pb-sn:a4-diamond  
_tdb: _tdb:PbSn-17Gie.tdb:DIAMOND_A4, tdb:PbSn-22Khv-3g.tdb:DIAMOND_A4, tdb:PbSn-95Oht-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[PbSn-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-17Gie.tdb): DIAMOND_A4, type code %, sha256 `7a442ed9f5eb5e7a…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

[PbSn-22Khv-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-22Khv-3g.tdb): DIAMOND_A4, type code %, sha256 `cc698ce94556d47f…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : SN : !
~~~~

[PbSn-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-95Oht-LB.tdb): DIAMOND_A4, type code %, sha256 `04c045f1bd0a9b7e…`

~~~~text
57: PHASE DIAMOND_A4 % 1 1 !
58: CONST DIAMOND_A4 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102396](https://doi.org/10.1016/j.calphad.2022.102396) A.V. Khvan, A.T. Dinsdale, Q. Chen, Calphad, 76, 102396(2022).  
_assessment that models this phase_

## BCT_A5 (Pb–Sn)

- Id: `phase:pb-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 0.97537–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sn:a5-bct)

Names (4): _corpus: _corpus:phase:pb-sn:a5-bct  
_tdb: _tdb:PbSn-17Gie.tdb:BCT_A5, tdb:PbSn-22Khv-3g.tdb:BCT_A5, tdb:PbSn-95Oht-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (3): PHASE and CONSTITUENT statements as written

[PbSn-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-17Gie.tdb): BCT_A5, type code %, sha256 `7a442ed9f5eb5e7a…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : PB SN% : !
~~~~

[PbSn-22Khv-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-22Khv-3g.tdb): BCT_A5, type code %, sha256 `cc698ce94556d47f…`

~~~~text
57: PHASE BCT_A5 % 1 1.545977367 !
58: CONST BCT_A5 : PB SN% : !
~~~~

[PbSn-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-95Oht-LB.tdb): BCT_A5, type code %, sha256 `04c045f1bd0a9b7e…`

~~~~text
62: PHASE BCT_A5 % 1 1 !
63: CONST BCT_A5 : PB SN% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102396](https://doi.org/10.1016/j.calphad.2022.102396) A.V. Khvan, A.T. Dinsdale, Q. Chen, Calphad, 76, 102396(2022).  
_assessment that models this phase_

## BCC_A2 (Pb–Sn)

- Id: `phase:pb-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sn:bcc-a2)

Names (3): _corpus: _corpus:phase:pb-sn:bcc-a2  
_tdb: _tdb:PbSn-17Gie.tdb:BCC_A2, tdb:PbSn-95Oht-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PbSn-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-17Gie.tdb): BCC_A2, type code %B, sha256 `7a442ed9f5eb5e7a…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : PB SN : VA : !
~~~~

[PbSn-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-95Oht-LB.tdb): BCC_A2, type code %B, sha256 `04c045f1bd0a9b7e…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : PB SN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_

## FCC_A1 (Pb–Sn)

- Id: `phase:pb-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–600.61 K, x(Sn) 0–0.30618
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sn:fcc-a1)

Names (4): _corpus: _corpus:phase:pb-sn:fcc-a1  
_tdb: _tdb:PbSn-17Gie.tdb:FCC_A1, tdb:PbSn-22Khv-3g.tdb:FCC_A1, tdb:PbSn-95Oht-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[PbSn-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-17Gie.tdb): FCC_A1, type code %A, sha256 `7a442ed9f5eb5e7a…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : PB% SN : VA : !
~~~~

[PbSn-22Khv-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-22Khv-3g.tdb): FCC_A1, type code %A, sha256 `cc698ce94556d47f…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : PB% SN : VA : !
~~~~

[PbSn-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-95Oht-LB.tdb): FCC_A1, type code %A, sha256 `04c045f1bd0a9b7e…`

~~~~text
42: PHASE FCC_A1 %A 2 1 1 !
43: CONST FCC_A1 : PB% SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102396](https://doi.org/10.1016/j.calphad.2022.102396) A.V. Khvan, A.T. Dinsdale, Q. Chen, Calphad, 76, 102396(2022).  
_assessment that models this phase_

## HCP_A3 (Pb–Sn)

- Id: `phase:pb-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sn:hcp-a3)

Names (4): _corpus: _corpus:phase:pb-sn:hcp-a3  
_tdb: _tdb:PbSn-17Gie.tdb:HCP_A3, tdb:PbSn-22Khv-3g.tdb:HCP_A3, tdb:PbSn-95Oht-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[PbSn-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-17Gie.tdb): HCP_A3, type code %A, sha256 `7a442ed9f5eb5e7a…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : PB SN : VA : !
~~~~

[PbSn-22Khv-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-22Khv-3g.tdb): HCP_A3, type code %A, sha256 `cc698ce94556d47f…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : PB SN : VA : !
~~~~

[PbSn-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-95Oht-LB.tdb): HCP_A3, type code %A, sha256 `04c045f1bd0a9b7e…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : PB SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102396](https://doi.org/10.1016/j.calphad.2022.102396) A.V. Khvan, A.T. Dinsdale, Q. Chen, Calphad, 76, 102396(2022).  
_assessment that models this phase_

## LIQUID (Pb–Sn)

- Id: `phase:pb-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 455.69–2500 K, x(Sn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sn:liquid)

Names (4): _corpus: _corpus:phase:pb-sn:liquid  
_tdb: _tdb:PbSn-17Gie.tdb:LIQUID, tdb:PbSn-22Khv-3g.tdb:LIQUID, tdb:PbSn-95Oht-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[PbSn-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-17Gie.tdb): LIQUID, type code %, sha256 `7a442ed9f5eb5e7a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : PB SN : !
~~~~

[PbSn-22Khv-3g.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-22Khv-3g.tdb): LIQUID, type code %, sha256 `cc698ce94556d47f…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : PB SN : !
~~~~

[PbSn-95Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSn-95Oht-LB.tdb): LIQUID, type code %, sha256 `04c045f1bd0a9b7e…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : PB SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02645349](https://doi.org/10.1007/BF02645349) H. Ohtani, K. Okuda, K. Ishida, J. Phase Equilib., 16, 416-29(1995).  
_assessment that models this phase_
- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2022.102396](https://doi.org/10.1016/j.calphad.2022.102396) A.V. Khvan, A.T. Dinsdale, Q. Chen, Calphad, 76, 102396(2022).  
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
