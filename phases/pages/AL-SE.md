# Al–Se phases

> Al–Se system: 6 phases (tier A 4, tier C 1, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-SE.html · Markdown: https://data.orchid-project.org/phases/pages/AL-SE.md

6 phases (tier A 4, tier C 1, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-SE) · [full JSON](https://data.orchid-project.org/phases/systems/AL-SE.json) · [Al–Se system page](https://data.orchid-project.org/systems/AL-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Se system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-al-se-a8-hexagonal); _phase:al-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1 | 2 | 1 |
| [AL2SE3](#phase-al-se-al2se3); _phase:al-se:al2se3_ | beta-Ga2Se3 · mC20 · Cc (9) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1207.32 K, x(Se) 0.6–0.6 | 13 | 1 |
| [BCC_A2](#phase-al-se-bcc-a2); _phase:al-se:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-al-se-fcc-a1); _phase:al-se:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–944.34 K, x(Se) 0–0 | 3 | 1 |
| [HCP_A3](#phase-al-se-hcp-a3); _phase:al-se:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-al-se-liquid); _phase:al-se:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 494–2500 K, x(Se) 0–1 | 5 | 1 |

## HEXAGONAL_A8 (Al–Se)

- Id: `phase:al-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-se:a8-hexagonal)

Names (4): _corpus: _corpus:phase:al-se:a8-hexagonal, corpus:phase:al-se:hexagonal-a8  
_paper: _paper:10.1007/s11669-019-00733-z:(Se)  
_tdb: _tdb:AlSe-19Shi.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[AlSe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSe-19Shi.tdb): HEXAGONAL_A8, type code %, sha256 `990a49c151cafe47…`

~~~~text
52: PHASE HEXAGONAL_A8 % 1 1 !
53: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_

## AL2SE3 (Al–Se)

- Id: `phase:al-se:al2se3`; status `assigned`
- Structure: beta-Ga2Se3 · mC20 · Cc (9); type `st:beta-ga2se3-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.4000, Se 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1207.32 K, x(Se) 0.6–0.6
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-se:al2se3)

Names (3): _corpus: _corpus:phase:al-se:al2se3  
_paper: _paper:10.1007/s11669-019-00733-z:Al2Se3  
_tdb: _tdb:AlSe-19Shi.tdb:AL2SE3  


### TDB models of AL2SE3 (1): PHASE and CONSTITUENT statements as written

[AlSe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSe-19Shi.tdb): AL2SE3, type code %, sha256 `990a49c151cafe47…`

~~~~text
57: PHASE AL2SE3 % 2 2 3 !
58: CONST AL2SE3 : AL : SE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1107/s0365110x66001506](https://doi.org/10.1107/s0365110x66001506) G. A. Steigmann, J. Goodyear, The crystal structure of Al\<sub>2\</sub>Se\<sub>3\</sub>, Acta Cryst 20, 617-619 (1966).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19542770107](https://doi.org/10.1002/zaac.19542770107) A. Schneider, G. Gattow, Beitrag zum System Aluminium–Selen, Zeitschrift anorg allge chemie 277, 49-59 (1954).  
_cited as the source of values for this phase_

## BCC_A2 (Al–Se)

- Id: `phase:al-se:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-se:bcc-a2)

Names (2): _corpus: _corpus:phase:al-se:bcc-a2  
_tdb: _tdb:AlSe-19Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AlSe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSe-19Shi.tdb): BCC_A2, type code %B, sha256 `990a49c151cafe47…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : AL : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase_

## FCC_A1 (Al–Se)

- Id: `phase:al-se:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–944.34 K, x(Se) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-se:fcc-a1)

Names (3): _corpus: _corpus:phase:al-se:fcc-a1  
_paper: _paper:10.1007/s11669-019-00733-z:(αAl)  
_tdb: _tdb:AlSe-19Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AlSe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSe-19Shi.tdb): FCC_A1, type code %A, sha256 `990a49c151cafe47…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : AL : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Al–Se)

- Id: `phase:al-se:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-se:hcp-a3)

Names (2): _corpus: _corpus:phase:al-se:hcp-a3  
_tdb: _tdb:AlSe-19Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AlSe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSe-19Shi.tdb): HCP_A3, type code %A, sha256 `990a49c151cafe47…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : AL : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase_

## LIQUID (Al–Se)

- Id: `phase:al-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 494–2500 K, x(Se) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-se:liquid)

Names (3): _corpus: _corpus:phase:al-se:liquid  
_paper: _paper:10.1007/s11669-019-00733-z:L  
_tdb: _tdb:AlSe-19Shi.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AlSe-19Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AlSe-19Shi.tdb): LIQUID, type code %, sha256 `990a49c151cafe47…`

~~~~text
32: PHASE LIQUID % 1 1 !
33: CONST LIQUID : AL SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-019-00733-z](https://doi.org/10.1007/s11669-019-00733-z) Chenying Shi, Biaobiao Yang, Biao Hu, Yong Du, Sheng Yao, Thermodynamic Description of the Al–X (X = S, Se, Te) Systems, J. Phase Equilib. Diffus. 40, 392-402 (2019).  
_assessment that models this phase; reports values for this phase_

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
