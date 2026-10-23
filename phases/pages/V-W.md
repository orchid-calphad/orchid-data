# V–W phases

> V–W system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/V-W.html · Markdown: https://data.orchid-project.org/phases/pages/V-W.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=V-W) · [full JSON](https://data.orchid-project.org/phases/systems/V-W.json) · [V–W system page](https://data.orchid-project.org/systems/V-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/V-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the V–W system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-v-w-bcc-a2); _phase:v-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0–1 | 0 | 2 |
| [FCC_A1](#phase-v-w-fcc-a1); _phase:v-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-v-w-hcp-a3); _phase:v-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-v-w-liquid); _phase:v-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2150.5–4000 K, x(W) 0–1 | 0 | 2 |

## BCC_A2 (V–W)

- Id: `phase:v-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-w:bcc-a2)

Names (3): _corpus: _corpus:phase:v-w:bcc-a2  
_tdb: _tdb:VW-05Bra-LB.tdb:BCC_A2, tdb:VW-05Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[VW-05Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VW-05Bra-LB.tdb): BCC_A2, type code %B, sha256 `50a89a7b166d5a96…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : V% W% : VA : !
~~~~

[VW-05Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VW-05Hua.tdb): BCC_A2, type code %B, sha256 `7d259ad62b6c6f76…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : V% W% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2004.11.047](https://doi.org/10.1016/j.jallcom.2004.11.047) S. Huang, J. Vleugels, L. Li, O. Van der Biest, J. Alloys Compd., 395, 68-74(2005).  
_assessment that models this phase_
- [doi:10.3139/146.018120](https://doi.org/10.3139/146.018120) J. Bratberg, Z. Metallkd., 96, 335-44(2005).  
_assessment that models this phase_

## FCC_A1 (V–W)

- Id: `phase:v-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-w:fcc-a1)

Names (3): _corpus: _corpus:phase:v-w:fcc-a1  
_tdb: _tdb:VW-05Bra-LB.tdb:FCC_A1, tdb:VW-05Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[VW-05Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VW-05Bra-LB.tdb): FCC_A1, type code %A, sha256 `50a89a7b166d5a96…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : V W : VA : !
~~~~

[VW-05Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VW-05Hua.tdb): FCC_A1, type code %A, sha256 `7d259ad62b6c6f76…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : V W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2004.11.047](https://doi.org/10.1016/j.jallcom.2004.11.047) S. Huang, J. Vleugels, L. Li, O. Van der Biest, J. Alloys Compd., 395, 68-74(2005).  
_assessment that models this phase_
- [doi:10.3139/146.018120](https://doi.org/10.3139/146.018120) J. Bratberg, Z. Metallkd., 96, 335-44(2005).  
_assessment that models this phase_

## HCP_A3 (V–W)

- Id: `phase:v-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-w:hcp-a3)

Names (3): _corpus: _corpus:phase:v-w:hcp-a3  
_tdb: _tdb:VW-05Bra-LB.tdb:HCP_A3, tdb:VW-05Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[VW-05Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VW-05Bra-LB.tdb): HCP_A3, type code %A, sha256 `50a89a7b166d5a96…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : V W : VA : !
~~~~

[VW-05Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VW-05Hua.tdb): HCP_A3, type code %A, sha256 `7d259ad62b6c6f76…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : V W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2004.11.047](https://doi.org/10.1016/j.jallcom.2004.11.047) S. Huang, J. Vleugels, L. Li, O. Van der Biest, J. Alloys Compd., 395, 68-74(2005).  
_assessment that models this phase_
- [doi:10.3139/146.018120](https://doi.org/10.3139/146.018120) J. Bratberg, Z. Metallkd., 96, 335-44(2005).  
_assessment that models this phase_

## LIQUID (V–W)

- Id: `phase:v-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2150.5–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-w:liquid)

Names (3): _corpus: _corpus:phase:v-w:liquid  
_tdb: _tdb:VW-05Bra-LB.tdb:LIQUID, tdb:VW-05Hua.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[VW-05Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VW-05Bra-LB.tdb): LIQUID, type code %, sha256 `50a89a7b166d5a96…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : V W : !
~~~~

[VW-05Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/VW-05Hua.tdb): LIQUID, type code %, sha256 `7d259ad62b6c6f76…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : V W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2004.11.047](https://doi.org/10.1016/j.jallcom.2004.11.047) S. Huang, J. Vleugels, L. Li, O. Van der Biest, J. Alloys Compd., 395, 68-74(2005).  
_assessment that models this phase_
- [doi:10.3139/146.018120](https://doi.org/10.3139/146.018120) J. Bratberg, Z. Metallkd., 96, 335-44(2005).  
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
