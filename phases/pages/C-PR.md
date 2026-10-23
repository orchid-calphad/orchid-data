# C–Pr phases

> C–Pr system: 8 phases (tier A 6, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-PR.html · Markdown: https://data.orchid-project.org/phases/pages/C-PR.md

8 phases (tier A 6, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-PR) · [full JSON](https://data.orchid-project.org/phases/systems/C-PR.json) · [C–Pr system page](https://data.orchid-project.org/systems/C-PR.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-PR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Pr system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-pr-a4-diamond); _phase:c-pr:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GRAPHITE_A9](#phase-c-pr-a9-graphite); _phase:c-pr:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 1 |
| [BCC_A2](#phase-c-pr-bcc-a2); _phase:c-pr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 948.99–2429 K, x(C) 0–0.0773 | 0 | 1 |
| [DHCP](#phase-c-pr-dhcp-a3); _phase:c-pr:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1153 K, x(C) 0–0.04431 | 0 | 1 |
| [LIQUID](#phase-c-pr-liquid); _phase:c-pr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1072.12–4000 K, x(C) 0–0.86142 | 0 | 1 |
| [PR2C3_D5C](#phase-c-pr-pr2c3-d5c); _phase:c-pr:pr2c3-d5c_ | Pu2C3 · D5_c · cI40 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1821.15 K, x(C) 0.54404–0.6 | 0 | 1 |
| [PRC2_BETA](#phase-c-pr-prc2-beta); _phase:c-pr:prc2-beta_ | CaC2 · cF36 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1427.43–2589.18 K, x(C) 0.65795–0.66612 | 0 | 1 |
| [PRC2_C11A](#phase-c-pr-prc2-c11a); _phase:c-pr:prc2-c11a_ | CaC2 · C11_a · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1413.6 K, x(C) 0.66667–0.66667 | 0 | 1 |

## DIAMOND_A4 (C–Pr)

- Id: `phase:c-pr:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pr:a4-diamond)

Names (2): _corpus: _corpus:phase:c-pr:a4-diamond  
_tdb: _tdb:PrC-11Pen.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[PrC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb): DIAMOND_A4, type code %, sha256 `7207a325d93d7b08…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Pr)

- Id: `phase:c-pr:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pr:a9-graphite)

Names (2): _corpus: _corpus:phase:c-pr:a9-graphite  
_tdb: _tdb:PrC-11Pen.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (1): PHASE and CONSTITUENT statements as written

[PrC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb): GRAPHITE_A9, type code %, sha256 `7207a325d93d7b08…`

~~~~text
51: PHASE GRAPHITE_A9 % 1 1 !
52: CONST GRAPHITE_A9 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## BCC_A2 (C–Pr)

- Id: `phase:c-pr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 948.99–2429 K, x(C) 0–0.0773
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pr:bcc-a2)

Names (2): _corpus: _corpus:phase:c-pr:bcc-a2  
_tdb: _tdb:PrC-11Pen.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PrC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb): BCC_A2, type code %B, sha256 `7207a325d93d7b08…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : PR : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## DHCP (C–Pr)

- Id: `phase:c-pr:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1153 K, x(C) 0–0.04431
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pr:dhcp-a3)

Names (2): _corpus: _corpus:phase:c-pr:dhcp-a3  
_tdb: _tdb:PrC-11Pen.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[PrC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb): DHCP, type code %, sha256 `7207a325d93d7b08…`

~~~~text
41: PHASE DHCP % 2 1 1 !
42: CONST DHCP : PR : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## LIQUID (C–Pr)

- Id: `phase:c-pr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1072.12–4000 K, x(C) 0–0.86142
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pr:liquid)

Names (2): _corpus: _corpus:phase:c-pr:liquid  
_tdb: _tdb:PrC-11Pen.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PrC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb): LIQUID, type code %, sha256 `7207a325d93d7b08…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : C PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## PR2C3_D5C (C–Pr)

- Id: `phase:c-pr:pr2c3-d5c`; status `assigned`
- Structure: Pu2C3 · D5_c · cI40 · I-43d (220); type `st:d5-c-pu2c3-ci40`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1821.15 K, x(C) 0.54404–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pr:pr2c3-d5c)

Names (2): _corpus: _corpus:phase:c-pr:pr2c3-d5c  
_tdb: _tdb:PrC-11Pen.tdb:PR2C3_D5C  


### TDB models of PR2C3_D5C (1): PHASE and CONSTITUENT statements as written

[PrC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb): PR2C3_D5C, type code %, sha256 `7207a325d93d7b08…`

~~~~text
56: PHASE PR2C3_D5C % 2 2 3 !
57: CONST PR2C3_D5C : PR : C% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## PRC2_BETA (C–Pr)

- Id: `phase:c-pr:prc2-beta`; status `assigned`
- Structure: CaC2 · cF36 · Fm-3m (225); type `st:cac2-cf36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 1427.43–2589.18 K, x(C) 0.65795–0.66612
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pr:prc2-beta)

Names (2): _corpus: _corpus:phase:c-pr:prc2-beta  
_tdb: _tdb:PrC-11Pen.tdb:PRC2_BETA  


### TDB models of PRC2_BETA (1): PHASE and CONSTITUENT statements as written

[PrC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb): PRC2_BETA, type code %, sha256 `7207a325d93d7b08…`

~~~~text
66: PHASE PRC2_BETA % 2 1 2 !
67: CONST PRC2_BETA : PR : C% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## PRC2_C11A (C–Pr)

- Id: `phase:c-pr:prc2-c11a`; status `assigned`
- Structure: CaC2 · C11_a · tI6 · I4/mmm (139); type `st:c11-a-cac2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: C 0.6667, Pr 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1413.6 K, x(C) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-pr:prc2-c11a)

Names (2): _corpus: _corpus:phase:c-pr:prc2-c11a  
_tdb: _tdb:PrC-11Pen.tdb:PRC2_C11A  


### TDB models of PRC2_C11A (1): PHASE and CONSTITUENT statements as written

[PrC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/PrC-11Pen.tdb): PRC2_C11A, type code %, sha256 `7207a325d93d7b08…`

~~~~text
61: PHASE PRC2_C11A % 2 1 2 !
62: CONST PRC2_C11A : PR : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
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
