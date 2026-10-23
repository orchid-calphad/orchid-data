# Ce–Ti phases

> Ce–Ti system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-TI.html · Markdown: https://data.orchid-project.org/phases/pages/CE-TI.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-TI) · [full JSON](https://data.orchid-project.org/phases/systems/CE-TI.json) · [Ce–Ti system page](https://data.orchid-project.org/systems/CE-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Ti system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-ti-bcc-a2); _phase:ce-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 301.24–2499.73 K, x(Ti) 0–1 | 0 | 1 |
| [FCC_A1](#phase-ce-ti-fcc-a1); _phase:ce-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Ti) 0–0 | 0 | 1 |
| [HCP_A3](#phase-ce-ti-hcp-a3); _phase:ce-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1190 K, x(Ti) 0.23–1 | 0 | 1 |
| [LIQUID](#phase-ce-ti-liquid); _phase:ce-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1060.03–2500 K, x(Ti) 0–1 | 0 | 1 |

## BCC_A2 (Ce–Ti)

- Id: `phase:ce-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 301.24–2499.73 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-ti:bcc-a2)

Names (2): _corpus: _corpus:phase:ce-ti:bcc-a2  
_tdb: _tdb:CeTi-18Yao.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CeTi-18Yao.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTi-18Yao.tdb): BCC_A2, type code %B, sha256 `775e4e88db0a2957…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CE% TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0) Bin Yao, Biao Hu, Anan Zhang, Jingrui Zhao, Jiong Wang, Yong Du, Thermodynamic Assessment of the Ti-RE (RE = Ce, Er, Tm, Y) Binary Systems, J. Phase Equilib. Diffus. 39, 44-50 (2018).  
_assessment that models this phase_

## FCC_A1 (Ce–Ti)

- Id: `phase:ce-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Ti) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-ti:fcc-a1)

Names (2): _corpus: _corpus:phase:ce-ti:fcc-a1  
_tdb: _tdb:CeTi-18Yao.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CeTi-18Yao.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTi-18Yao.tdb): FCC_A1, type code %A, sha256 `775e4e88db0a2957…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CE% TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0) Bin Yao, Biao Hu, Anan Zhang, Jingrui Zhao, Jiong Wang, Yong Du, Thermodynamic Assessment of the Ti-RE (RE = Ce, Er, Tm, Y) Binary Systems, J. Phase Equilib. Diffus. 39, 44-50 (2018).  
_assessment that models this phase_

## HCP_A3 (Ce–Ti)

- Id: `phase:ce-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1190 K, x(Ti) 0.23–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-ti:hcp-a3)

Names (2): _corpus: _corpus:phase:ce-ti:hcp-a3  
_tdb: _tdb:CeTi-18Yao.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CeTi-18Yao.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTi-18Yao.tdb): HCP_A3, type code %A, sha256 `775e4e88db0a2957…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CE TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0) Bin Yao, Biao Hu, Anan Zhang, Jingrui Zhao, Jiong Wang, Yong Du, Thermodynamic Assessment of the Ti-RE (RE = Ce, Er, Tm, Y) Binary Systems, J. Phase Equilib. Diffus. 39, 44-50 (2018).  
_assessment that models this phase_

## LIQUID (Ce–Ti)

- Id: `phase:ce-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1060.03–2500 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-ti:liquid)

Names (2): _corpus: _corpus:phase:ce-ti:liquid  
_tdb: _tdb:CeTi-18Yao.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CeTi-18Yao.tdb](https://orchid-project.org/data/databases/sgte-binary/CeTi-18Yao.tdb): LIQUID, type code %, sha256 `775e4e88db0a2957…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CE TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-017-0605-0](https://doi.org/10.1007/s11669-017-0605-0) Bin Yao, Biao Hu, Anan Zhang, Jingrui Zhao, Jiong Wang, Yong Du, Thermodynamic Assessment of the Ti-RE (RE = Ce, Er, Tm, Y) Binary Systems, J. Phase Equilib. Diffus. 39, 44-50 (2018).  
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
