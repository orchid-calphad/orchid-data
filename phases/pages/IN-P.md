# In–P phases

> In–P system: 9 phases (tier A 5, liquid 1, gas 1, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-P.html · Markdown: https://data.orchid-project.org/phases/pages/IN-P.md

9 phases (tier A 5, liquid 1, gas 1, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-P) · [full JSON](https://data.orchid-project.org/phases/systems/IN-P.json) · [In–P system page](https://data.orchid-project.org/systems/IN-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–P system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-p-a6-tetragonal); _phase:in-p:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(P) 0–0 | 0 | 1 |
| [ZINCBLENDE_B3](#phase-in-p-b3-zincblende); _phase:in-p:b3-zincblende_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1275.75 K, x(P) 0.5–0.5 | 0 | 1 |
| [BCC_A2](#phase-in-p-bcc-a2); _phase:in-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-in-p-fcc-a1); _phase:in-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-in-p-gas); _phase:in-p:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 704.7–2500 K, x(P) 0–1 | 0 | 1 |
| [HCP_A3](#phase-in-p-hcp-a3); _phase:in-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-in-p-liquid); _phase:in-p:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–2293.45 K, x(P) 0–0.24696 | 0 | 1 |
| [RED_P](#phase-in-p-p-red); _phase:in-p:p-red_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–704.7 K, x(P) 1–1 | 0 | 1 |
| [WHITE_P](#phase-in-p-p-white); _phase:in-p:p-white_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## TETRAGONAL_A6 (In–P)

- Id: `phase:in-p:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(P) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-p:a6-tetragonal  
_tdb: _tdb:InP-94Ans-LB.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): TETRAGONAL_A6, type code %, sha256 `f70a0661ae375193…`

~~~~text
55: PHASE TETRAGONAL_A6 % 1 1 !
56: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## ZINCBLENDE_B3 (In–P)

- Id: `phase:in-p:b3-zincblende`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabect and oqmd-646115, space group 216
- Stoichiometry: In 0.5000, P 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1275.75 K, x(P) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:b3-zincblende)

Names (4): _corpus: _corpus:phase:in-p:b3-zincblende  
_mp: _mp:mp-aaaabect  
_oqmd: _oqmd:oqmd-646115  
_tdb: _tdb:InP-94Ans-LB.tdb:ZINCBLENDE_B3  


### TDB models of ZINCBLENDE_B3 (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): ZINCBLENDE_B3, type code %, sha256 `f70a0661ae375193…`

~~~~text
70: PHASE ZINCBLENDE_B3 % 2 1 1 !
71: CONST ZINCBLENDE_B3 : IN : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## BCC_A2 (In–P)

- Id: `phase:in-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:bcc-a2)

Names (2): _corpus: _corpus:phase:in-p:bcc-a2  
_tdb: _tdb:InP-94Ans-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): BCC_A2, type code %B, sha256 `f70a0661ae375193…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : IN P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## FCC_A1 (In–P)

- Id: `phase:in-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:fcc-a1)

Names (2): _corpus: _corpus:phase:in-p:fcc-a1  
_tdb: _tdb:InP-94Ans-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): FCC_A1, type code %A, sha256 `f70a0661ae375193…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : IN P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## GAS (In–P)

- Id: `phase:in-p:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 704.7–2500 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:gas)

Names (2): _corpus: _corpus:phase:in-p:gas  
_tdb: _tdb:InP-94Ans-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): GAS, type code %, sha256 `f70a0661ae375193…`

~~~~text
73: PHASE GAS:G % 1 1 !
74: CONST GAS:G : IN IN2 INP P P2 P3 P4 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## HCP_A3 (In–P)

- Id: `phase:in-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:hcp-a3)

Names (2): _corpus: _corpus:phase:in-p:hcp-a3  
_tdb: _tdb:InP-94Ans-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): HCP_A3, type code %A, sha256 `f70a0661ae375193…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## LIQUID (In–P)

- Id: `phase:in-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–2293.45 K, x(P) 0–0.24696
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:liquid)

Names (2): _corpus: _corpus:phase:in-p:liquid  
_tdb: _tdb:InP-94Ans-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): LIQUID, type code %, sha256 `f70a0661ae375193…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : IN P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## RED_P (In–P)

- Id: `phase:in-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–704.7 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:p-red)

Names (2): _corpus: _corpus:phase:in-p:p-red  
_tdb: _tdb:InP-94Ans-LB.tdb:RED_P  


### TDB models of RED_P (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): RED_P, type code %, sha256 `f70a0661ae375193…`

~~~~text
65: PHASE RED_P % 1 1 !
66: CONST RED_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## WHITE_P (In–P)

- Id: `phase:in-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-p:p-white)

Names (2): _corpus: _corpus:phase:in-p:p-white  
_tdb: _tdb:InP-94Ans-LB.tdb:WHITE_P  


### TDB models of WHITE_P (1): PHASE and CONSTITUENT statements as written

[InP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InP-94Ans-LB.tdb): WHITE_P, type code %, sha256 `f70a0661ae375193…`

~~~~text
60: PHASE WHITE_P % 1 1 !
61: CONST WHITE_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
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
