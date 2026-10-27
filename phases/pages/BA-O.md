# Ba–O phases

> Ba–O system: 10 phases (tier A 4, liquid 2, gas 2, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BA-O.html · Markdown: https://data.orchid-project.org/phases/pages/BA-O.md

10 phases (tier A 4, liquid 2, gas 2, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BA-O) · [full JSON](https://data.orchid-project.org/phases/systems/BA-O.json) · [Ba–O system page](https://data.orchid-project.org/systems/BA-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/BA-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ba–O system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BAO](#phase-ba-o-bao); _phase:ba-o:bao_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2285.72 K, x(O) 0.5–0.66667 | 43 | 3 |
| [BAO_B1](#phase-ba-o-bao-b1); _phase:ba-o:bao-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | no calculated diagram | 0 | 2 |
| [BAO2_C11A](#phase-ba-o-bao2-c11a); _phase:ba-o:bao2-c11a_ |  | needs_review | no calculated diagram | 0 | 2 |
| [BCC_A2](#phase-ba-o-bcc-a2); _phase:ba-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1041.25 K, x(O) 0–0 | 0 | 3 |
| [FCC_A1](#phase-ba-o-fcc-a1); _phase:ba-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-ba-o-gas); _phase:ba-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 301.02–2500 K, x(O) 0–1 | 4 | 3 |
| [HCP_A3](#phase-ba-o-hcp-a3); _phase:ba-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 3 |
| [ION](#phase-ba-o-ion); _phase:ba-o:ion_ | liquid | liquid | no calculated diagram | 0 | 2 |
| [LIQUID](#phase-ba-o-liquid); _phase:ba-o:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 854.47–2500 K, x(O) 0–0.56843 | 6 | 1 |
| [O2GAS](#phase-ba-o-o2gas); _phase:ba-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–1181.02 K, x(O) 1–1 | 0 | 3 |

## BAO (Ba–O)

- Id: `phase:ba-o:bao`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_rows_disagree
- Candidate (dft_mp): Fm-3m (225) — on-hull MP BaO at x(O)=0.5000
- Candidate (dft_mp): I4/mmm (139) — on-hull MP BaO2 at x(O)=0.6667
- Candidate (dft_oqmd): R3 (146) — on-hull OQMD Ba1 O1 at x(O)=0.5000
- Candidate (dft_oqmd): C2/m (12) — on-hull OQMD Ba1 O2 at x(O)=0.6667
- Candidate (sgte_mmc2): NaCl · B1 · cF8 · Fm-3m (225) — Hallstedt 2025 mmc2 row for BAO: BaO (common model for BaO and BaO2)
- Candidate (sgte_mmc2): CaC2 · C11_a · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for BAO: BaO2 (common model for BaO and BaO2)
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — BaO-05Zho-mod.tdb: 'Prototype CaC2 (tI6, I4/mmm), C11_a, barium peroxide'
- Candidate (tdb_comment): NaCl · cF8 · Fm-3m — BaO-05Zho-mod.tdb: 'Prototype NaCl (cF8, Fm-3m), B1, barium oxide'
- Stability: stable in 1 of 1 calculated diagram(s): 300–2285.72 K, x(O) 0.5–0.66667
- Literature: 43 values (17 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:bao)

Names (9): _corpus: _corpus:phase:ba-o:bao  
_paper: _paper:10.1016/0364-5916(95)00012-4:BaO(G), paper:10.1016/0364-5916(95)00012-4:BaO(L), paper:10.1016/0364-5916(95)00012-4:BaO(S), paper:10.1016/0364-5916(95)00012-4:BaO2(S), paper:10.1111/j.1551-2916.2005.00368.x:BaO  
_tdb: _tdb:BaO-05Zho-mod.tdb:BAO, tdb:BaO-05Zho.tdb:BAO, tdb:BaO-95Zim.tdb:BAO  


### TDB models of BAO (3): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): BAO, type code %, sha256 `1166f495f723a413…`

~~~~text
76: PHASE BAO:I % 2 1 1 !
77: CONST BAO:I : BA+2 : O-2 O2-2 : !
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): BAO, type code %, sha256 `c272fdb1966d275b…`

~~~~text
62: PHASE BAO:I % 2 1 1 !
63: CONST BAO:I : BA+2 : O-2 O2-2 : !
~~~~

[BaO-95Zim.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb): BAO, type code %, sha256 `a0f7658f38a4a7d7…`

~~~~text
51: PHASE BAO % 1 1 !
52: CONST BAO : BAO BAO2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_assessment that models this phase; reports values for this phase_

## BAO_B1 (Ba–O)

- Id: `phase:ba-o:bao-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:bao-b1)

Names (3): _corpus: _corpus:phase:ba-o:bao-b1  
_tdb: _tdb:BaO-05Zho-mod.tdb:BAO_B1, tdb:BaO-05Zho.tdb:BAO_B1  


### TDB models of BAO_B1 (2): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): BAO_B1, type code %, sha256 `1166f495f723a413…`

~~~~text
81: PHASE BAO_B1:I % 2 1 1 !
82: CONST BAO_B1:I : BA+2 : O-2 O2-2 : !
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): BAO_B1, type code %, sha256 `c272fdb1966d275b…`

~~~~text
67: PHASE BAO_B1:I % 2 1 1 !
68: CONST BAO_B1:I : BA+2 : O-2 O2-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_assessment that models this phase_

## BAO2_C11A (Ba–O)

- Id: `phase:ba-o:bao2-c11a`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_C11_a; site_ratios_contradict_C11_a:BaO-05Zho-mod.tdb; site_ratios_contradict_C11_a:BaO-05Zho.tdb
- Candidate (name_token): CaC2 · C11_a · tI6 · I4/mmm (139) — Strukturbericht/word 'C11A' in the TDB name
- Candidate (sgte_mmc2): CaC2 · C11_a · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for BAO2_C11A: BaO2
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — BaO-05Zho-mod.tdb: 'Prototype CaC2 (tI6, I4/mmm), C11_a, barium peroxide'
- Candidate (tdb_comment): CaC2 · tI6 · I4/mmm — BaO-05Zho.tdb: 'Prototype CaC2 (tI6, I4/mmm), C11_a, barium peroxide'
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:bao2-c11a)

Names (3): _corpus: _corpus:phase:ba-o:bao2-c11a  
_tdb: _tdb:BaO-05Zho-mod.tdb:BAO2_C11A, tdb:BaO-05Zho.tdb:BAO2_C11A  


### TDB models of BAO2_C11A (2): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): BAO2_C11A, type code %, sha256 `1166f495f723a413…`

~~~~text
86: PHASE BAO2_C11A:I % 2 1 1 !
87: CONST BAO2_C11A:I : BA+2 : O-2 O2-2 : !
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): BAO2_C11A, type code %, sha256 `c272fdb1966d275b…`

~~~~text
72: PHASE BAO2_C11A:I % 2 1 1 !
73: CONST BAO2_C11A:I : BA+2 : O-2 O2-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_assessment that models this phase_

## BCC_A2 (Ba–O)

- Id: `phase:ba-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ba 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1041.25 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:bcc-a2)

Names (4): _corpus: _corpus:phase:ba-o:bcc-a2  
_tdb: _tdb:BaO-05Zho-mod.tdb:BCC_A2, tdb:BaO-05Zho.tdb:BCC_A2, tdb:BaO-95Zim.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): BCC_A2, type code %B, sha256 `1166f495f723a413…`

~~~~text
65: PHASE BCC_A2 %B 2 1 3 !
66: CONST BCC_A2 : BA : VA : !
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): BCC_A2, type code %B, sha256 `c272fdb1966d275b…`

~~~~text
51: PHASE BCC_A2 %B 2 1 3 !
52: CONST BCC_A2 : BA : VA : !
~~~~

[BaO-95Zim.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb): BCC_A2, type code %B, sha256 `a0f7658f38a4a7d7…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : BA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995).  
_assessment that models this phase_
- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_assessment that models this phase_

## FCC_A1 (Ba–O)

- Id: `phase:ba-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ba 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:fcc-a1)

Names (4): _corpus: _corpus:phase:ba-o:fcc-a1  
_tdb: _tdb:BaO-05Zho-mod.tdb:FCC_A1, tdb:BaO-05Zho.tdb:FCC_A1, tdb:BaO-95Zim.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): FCC_A1, type code %A, sha256 `1166f495f723a413…`

~~~~text
60: PHASE FCC_A1 %A 2 1 1 !
61: CONST FCC_A1 : BA : VA : !
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): FCC_A1, type code %A, sha256 `c272fdb1966d275b…`

~~~~text
46: PHASE FCC_A1 %A 2 1 1 !
47: CONST FCC_A1 : BA : VA : !
~~~~

[BaO-95Zim.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb): FCC_A1, type code %A, sha256 `a0f7658f38a4a7d7…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : BA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995).  
_assessment that models this phase_
- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_assessment that models this phase_

## GAS (Ba–O)

- Id: `phase:ba-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 301.02–2500 K, x(O) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:gas)

Names (6): _corpus: _corpus:phase:ba-o:gas  
_paper: _paper:10.1111/j.1551-2916.2005.00368.x:Gas, paper:10.1111/j.1551-2916.2005.00368.x:gas  
_tdb: _tdb:BaO-05Zho-mod.tdb:GAS, tdb:BaO-05Zho.tdb:GAS, tdb:BaO-95Zim.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): GAS, type code %, sha256 `1166f495f723a413…`

~~~~text
92: PHASE GAS:G % 1 1 !
93: CONST GAS:G : BA BA2 BA2O BAO O O2 O3 : !
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): GAS, type code %, sha256 `c272fdb1966d275b…`

~~~~text
78: PHASE GAS:G % 1 1 !
79: CONST GAS:G : BA BA2 BA2O BAO O O2 O3 : !
~~~~

[BaO-95Zim.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb): GAS, type code %, sha256 `a0f7658f38a4a7d7…`

~~~~text
57: PHASE GAS:G % 1 1 !
58: CONST GAS:G : BA BA2 BA2O BAO BA2O2 O O2 O3 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995).  
_assessment that models this phase_

## HCP_A3 (Ba–O)

- Id: `phase:ba-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ba 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:hcp-a3)

Names (4): _corpus: _corpus:phase:ba-o:hcp-a3  
_tdb: _tdb:BaO-05Zho-mod.tdb:HCP_A3, tdb:BaO-05Zho.tdb:HCP_A3, tdb:BaO-95Zim.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): HCP_A3, type code %A, sha256 `1166f495f723a413…`

~~~~text
70: PHASE HCP_A3 %A 2 1 0.5 !
71: CONST HCP_A3 : BA : VA : !
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): HCP_A3, type code %A, sha256 `c272fdb1966d275b…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : BA : VA : !
~~~~

[BaO-95Zim.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb): HCP_A3, type code %A, sha256 `a0f7658f38a4a7d7…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : BA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995).  
_assessment that models this phase_
- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_assessment that models this phase_

## ION (Ba–O)

- Id: `phase:ba-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:ion)

Names (3): _corpus: _corpus:phase:ba-o:ion  
_tdb: _tdb:BaO-05Zho-mod.tdb:ION, tdb:BaO-05Zho.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): ION, type code %, sha256 `1166f495f723a413…`

~~~~text
55: PHASE ION:Y % 2 1 1 !
56: CONST ION:Y : BA+2 : O-2 VA : !
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): ION, type code %, sha256 `c272fdb1966d275b…`

~~~~text
41: PHASE ION:Y % 2 1 1 !
42: CONST ION:Y : BA+2 : O-2 O2-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_assessment that models this phase_

## LIQUID (Ba–O)

- Id: `phase:ba-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 854.47–2500 K, x(O) 0–0.56843
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:liquid)

Names (4): _corpus: _corpus:phase:ba-o:liquid  
_paper: _paper:10.1111/j.1551-2916.2005.00368.x:L, paper:10.1111/j.1551-2916.2005.00368.x:liquid  
_tdb: _tdb:BaO-95Zim.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BaO-95Zim.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb): LIQUID, type code %, sha256 `a0f7658f38a4a7d7…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : BA BAO O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995).  
_assessment that models this phase_
- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
_reports values for this phase_

## O2GAS (Ba–O)

- Id: `phase:ba-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1181.02 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-o:o2gas)

Names (4): _corpus: _corpus:phase:ba-o:o2gas  
_tdb: _tdb:BaO-05Zho-mod.tdb:O2GAS, tdb:BaO-05Zho.tdb:O2GAS, tdb:BaO-95Zim.tdb:O2GAS  


### TDB models of O2GAS (3): PHASE and CONSTITUENT statements as written

[BaO-05Zho-mod.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho-mod.tdb): O2GAS, type code %, sha256 `1166f495f723a413…`

~~~~text
89: PHASE O2GAS % 1 1 !
90: CONST O2GAS : O2 :!
~~~~

[BaO-05Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-05Zho.tdb): O2GAS, type code %, sha256 `c272fdb1966d275b…`

~~~~text
75: PHASE O2GAS % 1 1 !
76: CONST O2GAS : O2 :!
~~~~

[BaO-95Zim.tdb](https://orchid-project.org/data/databases/sgte-binary/BaO-95Zim.tdb): O2GAS, type code %, sha256 `a0f7658f38a4a7d7…`

~~~~text
54: PHASE O2GAS % 1 1 !
55: CONST O2GAS : O2 :!
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00012-4](https://doi.org/10.1016/0364-5916%2895%2900012-4) E. Zimmermann, K. Hack, D. Neuschütz, Thermochemical assessment of the binary system Ba-O, Calphad 19, 119-127 (1995).  
_assessment that models this phase_
- [doi:10.1111/j.1551-2916.2005.00368.x](https://doi.org/10.1111/j.1551-2916.2005.00368.x) Shihuai Zhou, Raymundo Arroyave, Clive A. Randall, Zi‐Kui Liu, Thermodynamic Modeling of the Binary Barium–Oxygen System, Journal of the American Ceramic Society 88, 1943-1948 (2005).  
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
