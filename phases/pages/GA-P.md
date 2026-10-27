# Ga–P phases

> Ga–P system: 9 phases (tier A 5, liquid 1, gas 1, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-P.html · Markdown: https://data.orchid-project.org/phases/pages/GA-P.md

9 phases (tier A 5, liquid 1, gas 1, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-P) · [full JSON](https://data.orchid-project.org/phases/systems/GA-P.json) · [Ga–P system page](https://data.orchid-project.org/systems/GA-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–P system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-p-a11-orthorhombic); _phase:ga-p:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(P) 0–0 | 0 | 1 |
| [ZINCBLENDE_B3](#phase-ga-p-b3-zincblende); _phase:ga-p:b3-zincblende_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1657.43 K, x(P) 0.5–0.5 | 0 | 1 |
| [BCC_A2](#phase-ga-p-bcc-a2); _phase:ga-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ga-p-fcc-a1); _phase:ga-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-ga-p-gas); _phase:ga-p:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 704.7–2500 K, x(P) 0–1 | 0 | 1 |
| [HCP_A3](#phase-ga-p-hcp-a3); _phase:ga-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ga-p-liquid); _phase:ga-p:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.91–2471.6 K, x(P) 0–0.23038 | 0 | 1 |
| [RED_P](#phase-ga-p-p-red); _phase:ga-p:p-red_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–704.7 K, x(P) 1–1 | 0 | 1 |
| [WHITE_P](#phase-ga-p-p-white); _phase:ga-p:p-white_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## ORTHORHOMBIC_A11 (Ga–P)

- Id: `phase:ga-p:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(P) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:a11-orthorhombic)

Names (2): _corpus: _corpus:phase:ga-p:a11-orthorhombic  
_tdb: _tdb:GaP-94Ans-LB.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `392a70d39e558f62…`

~~~~text
50: PHASE ORTHORHOMBIC_A11 % 1 1 !
51: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## ZINCBLENDE_B3 (Ga–P)

- Id: `phase:ga-p:b3-zincblende`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadru and oqmd-7553, space group 216
- Stoichiometry: Ga 0.5000, P 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1657.43 K, x(P) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:b3-zincblende)

Names (4): _corpus: _corpus:phase:ga-p:b3-zincblende  
_mp: _mp:mp-aaaaadru  
_oqmd: _oqmd:oqmd-7553  
_tdb: _tdb:GaP-94Ans-LB.tdb:ZINCBLENDE_B3  


### TDB models of ZINCBLENDE_B3 (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): ZINCBLENDE_B3, type code %, sha256 `392a70d39e558f62…`

~~~~text
65: PHASE ZINCBLENDE_B3 % 2 1 1 !
66: CONST ZINCBLENDE_B3 : GA : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## BCC_A2 (Ga–P)

- Id: `phase:ga-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:bcc-a2)

Names (2): _corpus: _corpus:phase:ga-p:bcc-a2  
_tdb: _tdb:GaP-94Ans-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): BCC_A2, type code %B, sha256 `392a70d39e558f62…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : GA P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## FCC_A1 (Ga–P)

- Id: `phase:ga-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:fcc-a1)

Names (2): _corpus: _corpus:phase:ga-p:fcc-a1  
_tdb: _tdb:GaP-94Ans-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): FCC_A1, type code %A, sha256 `392a70d39e558f62…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : GA P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## GAS (Ga–P)

- Id: `phase:ga-p:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 704.7–2500 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:gas)

Names (2): _corpus: _corpus:phase:ga-p:gas  
_tdb: _tdb:GaP-94Ans-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): GAS, type code %, sha256 `392a70d39e558f62…`

~~~~text
68: PHASE GAS:G % 1 1 !
69: CONST GAS:G : GA GA2 GAP P P2 P3 P4 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## HCP_A3 (Ga–P)

- Id: `phase:ga-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:hcp-a3)

Names (2): _corpus: _corpus:phase:ga-p:hcp-a3  
_tdb: _tdb:GaP-94Ans-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): HCP_A3, type code %A, sha256 `392a70d39e558f62…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## LIQUID (Ga–P)

- Id: `phase:ga-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.91–2471.6 K, x(P) 0–0.23038
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:liquid)

Names (2): _corpus: _corpus:phase:ga-p:liquid  
_tdb: _tdb:GaP-94Ans-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): LIQUID, type code %, sha256 `392a70d39e558f62…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : GA P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## RED_P (Ga–P)

- Id: `phase:ga-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–704.7 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:p-red)

Names (2): _corpus: _corpus:phase:ga-p:p-red  
_tdb: _tdb:GaP-94Ans-LB.tdb:RED_P  


### TDB models of RED_P (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): RED_P, type code %, sha256 `392a70d39e558f62…`

~~~~text
60: PHASE RED_P % 1 1 !
61: CONST RED_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## WHITE_P (Ga–P)

- Id: `phase:ga-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-p:p-white)

Names (2): _corpus: _corpus:phase:ga-p:p-white  
_tdb: _tdb:GaP-94Ans-LB.tdb:WHITE_P  


### TDB models of WHITE_P (1): PHASE and CONSTITUENT statements as written

[GaP-94Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaP-94Ans-LB.tdb): WHITE_P, type code %, sha256 `392a70d39e558f62…`

~~~~text
55: PHASE WHITE_P % 1 1 !
56: CONST WHITE_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(94)90027-2](https://doi.org/10.1016/0364-5916%2894%2990027-2) I. Ansara, C. Chatillon, H.L. Lukas, T. Nishizawa, H. Ohtani, K. Ishida et al., A binary database for III–V compound semiconductor systems, Calphad 18, 177-222 (1994).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
