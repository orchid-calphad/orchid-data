# Co–In phases

> Co–In system: 7 phases (tier A 5, tier B 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-IN.html · Markdown: https://data.orchid-project.org/phases/pages/CO-IN.md

7 phases (tier A 5, tier B 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-IN) · [full JSON](https://data.orchid-project.org/phases/systems/CO-IN.json) · [Co–In system page](https://data.orchid-project.org/systems/CO-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–In system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-co-in-a6-tetragonal); _phase:co-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(In) 1–1 | 2 | 1 |
| [BCC_A2](#phase-co-in-bcc-a2); _phase:co-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [COIN2_CB](#phase-co-in-coin2-cb); _phase:co-in:coin2-cb_ | CuMg2 · C_b · oF48 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–824.26 K, x(In) 0.66667–0.66667 | 4 | 1 |
| [COIN3](#phase-co-in-coin3); _phase:co-in:coin3_ | In3Ir · tP16 · P4_2/mnm (136) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–765.21 K, x(In) 0.75–0.75 | 4 | 1 |
| [FCC_A1](#phase-co-in-fcc-a1); _phase:co-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 695–1782.86 K, x(In) 0–5e-05 | 4 | 1 |
| [HCP_A3](#phase-co-in-hcp-a3); _phase:co-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–695 K, x(In) 0–0 | 0 | 1 |
| [LIQUID](#phase-co-in-liquid); _phase:co-in:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(In) 0–1 | 8 | 1 |

## TETRAGONAL_A6 (Co–In)

- Id: `phase:co-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(In) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-in:a6-tetragonal)

Names (4): _corpus: _corpus:phase:co-in:a6-tetragonal, corpus:phase:co-in:tetragonal-a6  
_paper: _paper:10.1016/s0364-5916(02)00014-7:In  
_tdb: _tdb:CoIn-01Boa-LB.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[CoIn-01Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb): TETRAGONAL_A6, type code %, sha256 `7b7830ea54945b1a…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Co–In)

- Id: `phase:co-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-in:bcc-a2)

Names (2): _corpus: _corpus:phase:co-in:bcc-a2  
_tdb: _tdb:CoIn-01Boa-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CoIn-01Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb): BCC_A2, type code %B, sha256 `7b7830ea54945b1a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CO IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001).  
_assessment that models this phase_

## COIN2_CB (Co–In)

- Id: `phase:co-in:coin2-cb`; status `assigned`
- Structure: CuMg2 · C_b · oF48 · Fddd (70); type `st:c-b-cumg2-of48`; tier A: standard phase name; confidence high
- Stoichiometry: Co 0.3333, In 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–824.26 K, x(In) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-in:coin2-cb)

Names (3): _corpus: _corpus:phase:co-in:coin2-cb  
_paper: _paper:10.1016/s0364-5916(02)00014-7:CoIn2  
_tdb: _tdb:CoIn-01Boa-LB.tdb:COIN2_CB  


### TDB models of COIN2_CB (1): PHASE and CONSTITUENT statements as written

[CoIn-01Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb): COIN2_CB, type code %, sha256 `7b7830ea54945b1a…`

~~~~text
45: PHASE COIN2_CB % 2 1 2 !
46: CONST COIN2_CB : CO : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001).  
_assessment that models this phase; reports values for this phase_

## COIN3 (Co–In)

- Id: `phase:co-in:coin3`; status `assigned`
- Structure: In3Ir · tP16 · P4_2/mnm (136); type `st:in3ir-tp16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Co 0.2500, In 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–765.21 K, x(In) 0.75–0.75
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-in:coin3)

Names (5): _corpus: _corpus:phase:co-in:coin3  
_mp: _mp:mp-aaaabgxg  
_oqmd: _oqmd:oqmd-29374  
_paper: _paper:10.1016/s0364-5916(02)00014-7:CoIn3  
_tdb: _tdb:CoIn-01Boa-LB.tdb:COIN3  


### TDB models of COIN3 (1): PHASE and CONSTITUENT statements as written

[CoIn-01Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb): COIN3, type code %, sha256 `7b7830ea54945b1a…`

~~~~text
50: PHASE COIN3 % 2 1 3 !
51: CONST COIN3 : CO : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Co–In)

- Id: `phase:co-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 695–1782.86 K, x(In) 0–5e-05
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-in:fcc-a1)

Names (3): _corpus: _corpus:phase:co-in:fcc-a1  
_paper: _paper:10.1016/s0364-5916(02)00014-7:(αCo)  
_tdb: _tdb:CoIn-01Boa-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CoIn-01Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb): FCC_A1, type code %A, sha256 `7b7830ea54945b1a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CO% IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Co–In)

- Id: `phase:co-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–695 K, x(In) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-in:hcp-a3)

Names (2): _corpus: _corpus:phase:co-in:hcp-a3  
_tdb: _tdb:CoIn-01Boa-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CoIn-01Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb): HCP_A3, type code %A, sha256 `7b7830ea54945b1a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CO% IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001).  
_assessment that models this phase_

## LIQUID (Co–In)

- Id: `phase:co-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(In) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-in:liquid)

Names (3): _corpus: _corpus:phase:co-in:liquid  
_paper: _paper:10.1016/s0364-5916(02)00014-7:liq2  
_tdb: _tdb:CoIn-01Boa-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CoIn-01Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoIn-01Boa-LB.tdb): LIQUID, type code %, sha256 `7b7830ea54945b1a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CO IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(02)00014-7](https://doi.org/10.1016/S0364-5916%2802%2900014-7) D. Boa, B.K. Dongui, I. Ansara, Calphad, 25, 645-50(2001).  
_assessment that models this phase; reports values for this phase_

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
