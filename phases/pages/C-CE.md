# C–Ce phases

> C–Ce system: 10 phases (tier A 8, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-CE.html · Markdown: https://data.orchid-project.org/phases/pages/C-CE.md

10 phases (tier A 8, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-CE) · [full JSON](https://data.orchid-project.org/phases/systems/C-CE.json) · [C–Ce system page](https://data.orchid-project.org/systems/C-CE.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-CE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Ce system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-ce-a4-diamond); _phase:c-ce:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GRAPHITE_A9](#phase-c-ce-a9-graphite); _phase:c-ce:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 1 |
| [BCC_A2](#phase-c-ce-bcc-a2); _phase:c-ce:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1000–1132.09 K, x(C) 0–0.01369 | 0 | 1 |
| [CE2C3_D5C](#phase-c-ce-ce2c3-d5c); _phase:c-ce:ce2c3-d5c_ | Pu2C3 · D5_c · cI40 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1803.37 K, x(C) 0.6–0.6 | 0 | 1 |
| [CEC2_BETA](#phase-c-ce-cec2-beta); _phase:c-ce:cec2-beta_ | CaC2 · cF36 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 1374.22–2557.32 K, x(C) 0.66667–0.66667 | 0 | 1 |
| [CEC2_C11A](#phase-c-ce-cec2-c11a); _phase:c-ce:cec2-c11a_ | CaC2 · C11_a · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1374.22 K, x(C) 0.66667–0.66667 | 0 | 1 |
| [DHCP](#phase-c-ce-dhcp-a3); _phase:c-ce:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-c-ce-fcc-a1); _phase:c-ce:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1017.09 K, x(C) 0–0.04435 | 0 | 1 |
| [HCP_A3](#phase-c-ce-hcp-a3); _phase:c-ce:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-c-ce-liquid); _phase:c-ce:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 910.76–4000 K, x(C) 0–0.8493 | 0 | 1 |

## DIAMOND_A4 (C–Ce)

- Id: `phase:c-ce:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:a4-diamond)

Names (2): _corpus: _corpus:phase:c-ce:a4-diamond  
_tdb: _tdb:CeC-11Pen.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): DIAMOND_A4, type code %, sha256 `bf3abd58850a15ba…`

~~~~text
52: PHASE DIAMOND_A4 % 1 1 !
53: CONST DIAMOND_A4 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Ce)

- Id: `phase:c-ce:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:a9-graphite)

Names (2): _corpus: _corpus:phase:c-ce:a9-graphite  
_tdb: _tdb:CeC-11Pen.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): GRAPHITE_A9, type code %, sha256 `bf3abd58850a15ba…`

~~~~text
57: PHASE GRAPHITE_A9 % 1 1 !
58: CONST GRAPHITE_A9 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## BCC_A2 (C–Ce)

- Id: `phase:c-ce:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1000–1132.09 K, x(C) 0–0.01369
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:bcc-a2)

Names (2): _corpus: _corpus:phase:c-ce:bcc-a2  
_tdb: _tdb:CeC-11Pen.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): BCC_A2, type code %B, sha256 `bf3abd58850a15ba…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CE : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## CE2C3_D5C (C–Ce)

- Id: `phase:c-ce:ce2c3-d5c`; status `assigned`
- Structure: Pu2C3 · D5_c · cI40 · I-43d (220); type `st:d5-c-pu2c3-ci40`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdwf and oqmd-13369, space group 220
- Stoichiometry: C 0.6000, Ce 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1803.37 K, x(C) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:ce2c3-d5c)

Names (4): _corpus: _corpus:phase:c-ce:ce2c3-d5c  
_mp: _mp:mp-aaaabdwf  
_oqmd: _oqmd:oqmd-13369  
_tdb: _tdb:CeC-11Pen.tdb:CE2C3_D5C  


### TDB models of CE2C3_D5C (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): CE2C3_D5C, type code %, sha256 `bf3abd58850a15ba…`

~~~~text
62: PHASE CE2C3_D5C % 2 2 3 !
63: CONST CE2C3_D5C : CE : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## CEC2_BETA (C–Ce)

- Id: `phase:c-ce:cec2-beta`; status `assigned`
- Structure: CaC2 · cF36 · Fm-3m (225); type `st:cac2-cf36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: C 0.6667, Ce 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 1374.22–2557.32 K, x(C) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:cec2-beta)

Names (2): _corpus: _corpus:phase:c-ce:cec2-beta  
_tdb: _tdb:CeC-11Pen.tdb:CEC2_BETA  


### TDB models of CEC2_BETA (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): CEC2_BETA, type code %, sha256 `bf3abd58850a15ba…`

~~~~text
72: PHASE CEC2_BETA % 2 1 2 !
73: CONST CEC2_BETA : CE : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## CEC2_C11A (C–Ce)

- Id: `phase:c-ce:cec2-c11a`; status `assigned`
- Structure: CaC2 · C11_a · tI6 · I4/mmm (139); type `st:c11-a-cac2-ti6`; tier A: standard phase name; confidence high
- Stoichiometry: C 0.6667, Ce 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1374.22 K, x(C) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:cec2-c11a)

Names (2): _corpus: _corpus:phase:c-ce:cec2-c11a  
_tdb: _tdb:CeC-11Pen.tdb:CEC2_C11A  


### TDB models of CEC2_C11A (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): CEC2_C11A, type code %, sha256 `bf3abd58850a15ba…`

~~~~text
67: PHASE CEC2_C11A % 2 1 2 !
68: CONST CEC2_C11A : CE : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## DHCP (C–Ce)

- Id: `phase:c-ce:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:dhcp-a3)

Names (2): _corpus: _corpus:phase:c-ce:dhcp-a3  
_tdb: _tdb:CeC-11Pen.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): DHCP, type code %, sha256 `bf3abd58850a15ba…`

~~~~text
47: PHASE DHCP % 1 1 !
48: CONST DHCP : CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## FCC_A1 (C–Ce)

- Id: `phase:c-ce:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1017.09 K, x(C) 0–0.04435
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:fcc-a1)

Names (2): _corpus: _corpus:phase:c-ce:fcc-a1  
_tdb: _tdb:CeC-11Pen.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): FCC_A1, type code %A, sha256 `bf3abd58850a15ba…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CE : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## HCP_A3 (C–Ce)

- Id: `phase:c-ce:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:hcp-a3)

Names (2): _corpus: _corpus:phase:c-ce:hcp-a3  
_tdb: _tdb:CeC-11Pen.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): HCP_A3, type code %A, sha256 `bf3abd58850a15ba…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CE : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## LIQUID (C–Ce)

- Id: `phase:c-ce:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 910.76–4000 K, x(C) 0–0.8493
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ce:liquid)

Names (2): _corpus: _corpus:phase:c-ce:liquid  
_tdb: _tdb:CeC-11Pen.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CeC-11Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/CeC-11Pen.tdb): LIQUID, type code %, sha256 `bf3abd58850a15ba…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : C CE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.09.002](https://doi.org/10.1016/j.calphad.2011.09.002) Yingbiao Peng, Yong Du, Lijun Zhang, Chunsheng Sha, Shuhong Liu, Feng Zheng et al., Thermodynamic modeling of the C–RE (RE=La, Ce and Pr) systems, Calphad 35, 533-541 (2011).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
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
