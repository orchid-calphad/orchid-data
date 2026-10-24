# P–Sb phases

> P–Sb system: 8 phases (tier A 4, liquid 1, gas 1, needs_review 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/P-SB.html · Markdown: https://data.orchid-project.org/phases/pages/P-SB.md

8 phases (tier A 4, liquid 1, gas 1, needs_review 2); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=P-SB) · [full JSON](https://data.orchid-project.org/phases/systems/P-SB.json) · [Markdown](https://data.orchid-project.org/phases/pages/P-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the P–Sb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-p-sb-a7-rhombohedral); _phase:p-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(P) 0–0.00025 | 0 | 1 |
| [BCC_A2](#phase-p-sb-bcc-a2); _phase:p-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-p-sb-fcc-a1); _phase:p-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-p-sb-gas); _phase:p-sb:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 381.97–2500 K, x(P) 0–1 | 0 | 1 |
| [HCP_A3](#phase-p-sb-hcp-a3); _phase:p-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-p-sb-liquid); _phase:p-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 888.91–1830 K, x(P) 0–0.04251 | 0 | 1 |
| [RED_P](#phase-p-sb-p-red); _phase:p-sb:p-red_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–919.47 K, x(P) 1–1 | 0 | 1 |
| [WHITE_P](#phase-p-sb-p-white); _phase:p-sb:p-white_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## RHOMBOHEDRAL_A7 (P–Sb)

- Id: `phase:p-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(P) 0–0.00025
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sb:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:p-sb:a7-rhombohedral  
_tdb: _tdb:SbP-94Ans-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[SbP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbP-94Ans-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `d2d3f96ce75bac94…`

~~~~text
53: PHASE RHOMBOHEDRAL_A7 % 1 1 !
54: CONST RHOMBOHEDRAL_A7 : P SB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## BCC_A2 (P–Sb)

- Id: `phase:p-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sb:bcc-a2)

Names (2): _corpus: _corpus:phase:p-sb:bcc-a2  
_tdb: _tdb:SbP-94Ans-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SbP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbP-94Ans-LB.tdb): BCC_A2, type code %B, sha256 `d2d3f96ce75bac94…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : P SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## FCC_A1 (P–Sb)

- Id: `phase:p-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:p-sb:fcc-a1  
_tdb: _tdb:SbP-94Ans-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SbP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbP-94Ans-LB.tdb): FCC_A1, type code %A, sha256 `d2d3f96ce75bac94…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : P SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## GAS (P–Sb)

- Id: `phase:p-sb:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 381.97–2500 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sb:gas)

Names (2): _corpus: _corpus:phase:p-sb:gas  
_tdb: _tdb:SbP-94Ans-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SbP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbP-94Ans-LB.tdb): GAS, type code %, sha256 `d2d3f96ce75bac94…`

~~~~text
66: PHASE GAS:G % 1 1 !
67: CONST GAS:G : P P2 P3 P4 SB SB2 SB3 SB4 SBP SBP3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## HCP_A3 (P–Sb)

- Id: `phase:p-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sb:hcp-a3)

Names (2): _corpus: _corpus:phase:p-sb:hcp-a3  
_tdb: _tdb:SbP-94Ans-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SbP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbP-94Ans-LB.tdb): HCP_A3, type code %A, sha256 `d2d3f96ce75bac94…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## LIQUID (P–Sb)

- Id: `phase:p-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 888.91–1830 K, x(P) 0–0.04251
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sb:liquid)

Names (2): _corpus: _corpus:phase:p-sb:liquid  
_tdb: _tdb:SbP-94Ans-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SbP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbP-94Ans-LB.tdb): LIQUID, type code %, sha256 `d2d3f96ce75bac94…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : P SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## RED_P (P–Sb)

- Id: `phase:p-sb:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–919.47 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sb:p-red)

Names (2): _corpus: _corpus:phase:p-sb:p-red  
_tdb: _tdb:SbP-94Ans-LB.tdb:RED_P  


### TDB models of RED_P (1): PHASE and CONSTITUENT statements as written

[SbP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbP-94Ans-LB.tdb): RED_P, type code %, sha256 `d2d3f96ce75bac94…`

~~~~text
63: PHASE RED_P % 1 1 !
64: CONST RED_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## WHITE_P (P–Sb)

- Id: `phase:p-sb:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:p-sb:p-white)

Names (2): _corpus: _corpus:phase:p-sb:p-white  
_tdb: _tdb:SbP-94Ans-LB.tdb:WHITE_P  


### TDB models of WHITE_P (1): PHASE and CONSTITUENT statements as written

[SbP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbP-94Ans-LB.tdb): WHITE_P, type code %, sha256 `d2d3f96ce75bac94…`

~~~~text
58: PHASE WHITE_P % 1 1 !
59: CONST WHITE_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
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
