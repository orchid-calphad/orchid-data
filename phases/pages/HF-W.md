# Hf–W phases

> Hf–W system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-W.html · Markdown: https://data.orchid-project.org/phases/pages/HF-W.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-W) · [full JSON](https://data.orchid-project.org/phases/systems/HF-W.json) · [Hf–W system page](https://data.orchid-project.org/systems/HF-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–W system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-w-bcc-a2); _phase:hf-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0–1 | 0 | 2 |
| [C15_LAVES](#phase-hf-w-c15-laves); _phase:hf-w:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2806.23 K, x(W) 0.64626–0.66667 | 0 | 2 |
| [FCC_A1](#phase-hf-w-fcc-a1); _phase:hf-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-hf-w-hcp-a3); _phase:hf-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2531.02 K, x(W) 0–0.01514 | 0 | 2 |
| [LIQUID](#phase-hf-w-liquid); _phase:hf-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2213.68–4000 K, x(W) 0–1 | 0 | 2 |

## BCC_A2 (Hf–W)

- Id: `phase:hf-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-w:bcc-a2)

Names (3): _corpus: _corpus:phase:hf-w:bcc-a2  
_tdb: _tdb:HfW-02Sha-LB.tdb:BCC_A2, tdb:HfW-12Lie.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfW-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-02Sha-LB.tdb): BCC_A2, type code %B, sha256 `078db40d3d1acdff…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : HF W : VA : !
~~~~

[HfW-12Lie.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-12Lie.tdb): BCC_A2, type code %B, sha256 `8ac53fc523b76001…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : HF W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005) Alyson C. Lieser, Chelsey L. Zacherl, Arkapol Saengdeejing, Zi-Kui Liu, Laszlo J. Kecskes, First-principles calculations and thermodynamic re-modeling of the Hf–W system, Calphad 38, 92-99 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## C15_LAVES (Hf–W)

- Id: `phase:hf-w:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfW-02Sha-LB.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in HfW-12Lie.tdb also describes the disordered state
- Stability: stable in 2 of 2 calculated diagram(s): 300–2806.23 K, x(W) 0.64626–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-w:c15-laves)

Names (3): _corpus: _corpus:phase:hf-w:c15-laves  
_tdb: _tdb:HfW-02Sha-LB.tdb:C15_LAVES, tdb:HfW-12Lie.tdb:C15_LAVES  


### TDB models of C15_LAVES (2): PHASE and CONSTITUENT statements as written

[HfW-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-02Sha-LB.tdb): C15_LAVES, type code %, sha256 `078db40d3d1acdff…`

~~~~text
40: PHASE C15_LAVES % 2 2 1 !
41: CONST C15_LAVES : HF W% : HF% W : !
~~~~

[HfW-12Lie.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-12Lie.tdb): C15_LAVES, type code %, sha256 `8ac53fc523b76001…`

~~~~text
40: PHASE C15_LAVES % 2 2 1 !
41: CONST C15_LAVES : HF W% : HF% W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005) Alyson C. Lieser, Chelsey L. Zacherl, Arkapol Saengdeejing, Zi-Kui Liu, Laszlo J. Kecskes, First-principles calculations and thermodynamic re-modeling of the Hf–W system, Calphad 38, 92-99 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## FCC_A1 (Hf–W)

- Id: `phase:hf-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-w:fcc-a1)

Names (3): _corpus: _corpus:phase:hf-w:fcc-a1  
_tdb: _tdb:HfW-02Sha-LB.tdb:FCC_A1, tdb:HfW-12Lie.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HfW-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-02Sha-LB.tdb): FCC_A1, type code %A, sha256 `078db40d3d1acdff…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : HF W : VA : !
~~~~

[HfW-12Lie.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-12Lie.tdb): FCC_A1, type code %A, sha256 `8ac53fc523b76001…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : HF W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005) Alyson C. Lieser, Chelsey L. Zacherl, Arkapol Saengdeejing, Zi-Kui Liu, Laszlo J. Kecskes, First-principles calculations and thermodynamic re-modeling of the Hf–W system, Calphad 38, 92-99 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## HCP_A3 (Hf–W)

- Id: `phase:hf-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2531.02 K, x(W) 0–0.01514
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-w:hcp-a3)

Names (3): _corpus: _corpus:phase:hf-w:hcp-a3  
_tdb: _tdb:HfW-02Sha-LB.tdb:HCP_A3, tdb:HfW-12Lie.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HfW-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-02Sha-LB.tdb): HCP_A3, type code %A, sha256 `078db40d3d1acdff…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : HF% W : VA : !
~~~~

[HfW-12Lie.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-12Lie.tdb): HCP_A3, type code %A, sha256 `8ac53fc523b76001…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : HF% W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005) Alyson C. Lieser, Chelsey L. Zacherl, Arkapol Saengdeejing, Zi-Kui Liu, Laszlo J. Kecskes, First-principles calculations and thermodynamic re-modeling of the Hf–W system, Calphad 38, 92-99 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
_assessment that models this phase_

## LIQUID (Hf–W)

- Id: `phase:hf-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2213.68–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-w:liquid)

Names (3): _corpus: _corpus:phase:hf-w:liquid  
_tdb: _tdb:HfW-02Sha-LB.tdb:LIQUID, tdb:HfW-12Lie.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HfW-02Sha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-02Sha-LB.tdb): LIQUID, type code %, sha256 `078db40d3d1acdff…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : HF W : !
~~~~

[HfW-12Lie.tdb](https://orchid-project.org/data/databases/sgte-binary/HfW-12Lie.tdb): LIQUID, type code %, sha256 `8ac53fc523b76001…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : HF W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2012.04.005](https://doi.org/10.1016/j.calphad.2012.04.005) Alyson C. Lieser, Chelsey L. Zacherl, Arkapol Saengdeejing, Zi-Kui Liu, Laszlo J. Kecskes, First-principles calculations and thermodynamic re-modeling of the Hf–W system, Calphad 38, 92-99 (2012).  
_assessment that models this phase_
- [doi:10.1016/S0966-9795(02)00017-1](https://doi.org/10.1016/S0966-9795%2802%2900017-1) G. Shao, Intermetallics, 10, 429-34(2002).  
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
