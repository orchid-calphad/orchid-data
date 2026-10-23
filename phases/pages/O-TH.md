# O–Th phases

> O–Th system: 6 phases (tier A 3, liquid 2, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/O-TH.html · Markdown: https://data.orchid-project.org/phases/pages/O-TH.md

6 phases (tier A 3, liquid 2, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=O-TH) · [full JSON](https://data.orchid-project.org/phases/systems/O-TH.json) · [O–Th system page](https://data.orchid-project.org/systems/O-TH.html) · [Markdown](https://data.orchid-project.org/phases/pages/O-TH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the O–Th system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-o-th-bcc-a2); _phase:o-th:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1633.2–2022.99 K, x(O) 0–0 | 0 | 2 |
| [FCC_A1](#phase-o-th-fcc-a1); _phase:o-th:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1633.2 K, x(O) 0–0 | 0 | 2 |
| [ION](#phase-o-th-ion); _phase:o-th:ion_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2006.45–4000 K, x(O) 0–0.67229 | 0 | 2 |
| [LIQUID](#phase-o-th-liquid); _phase:o-th:liquid_ | liquid | liquid | not stable in 2 calculated diagram(s) | 6 | 2 |
| [O2GAS](#phase-o-th-o2gas); _phase:o-th:o2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(O) 1–1 | 0 | 2 |
| [THO2_C1](#phase-o-th-tho2-c1); _phase:o-th:tho2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3680.2 K, x(O) 0.65904–0.66667 | 0 | 2 |

## BCC_A2 (O–Th)

- Id: `phase:o-th:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Th 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 1633.2–2022.99 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-th:bcc-a2)

Names (3): _corpus: _corpus:phase:o-th:bcc-a2  
_tdb: _tdb:ThO-03Kin.tdb:BCC_A2, tdb:ThO-18Ber.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ThO-03Kin.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-03Kin.tdb): BCC_A2, type code %B, sha256 `640414db2a764520…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : TH : VA : !
~~~~

[ThO-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-18Ber.tdb): BCC_A2, type code %B, sha256 `7787fa4553bd2bc8…`

~~~~text
47: PHASE BCC_A2 %B 2 1 3 !
48: CONST BCC_A2 : TH : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2018.09.013](https://doi.org/10.1016/j.jnucmat.2018.09.013) A. Bergeron, D. Manara, O. Beneš, R. Eloirdi, M.H.A. Piro, E.C. Corcoran, Thermodynamic modelling of thoria-urania and thoria-plutonia fuels: Description of the Th-U-Pu-O quaternary system, Journal of Nuclear Materials 512, 324-348 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0021-9614(03)00002-8](https://doi.org/10.1016/S0021-9614%2803%2900002-8) H. Kinoshita, D. Setoyama, Y. Saito, M. Hirota, K. Kurosaki, M. Uno, S. Yamanaka, J. Chem. Thermodyn., 35, 719-31(2003).  
_assessment that models this phase_

## FCC_A1 (O–Th)

- Id: `phase:o-th:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Th 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1633.2 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-th:fcc-a1)

Names (3): _corpus: _corpus:phase:o-th:fcc-a1  
_tdb: _tdb:ThO-03Kin.tdb:FCC_A1, tdb:ThO-18Ber.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ThO-03Kin.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-03Kin.tdb): FCC_A1, type code %, sha256 `640414db2a764520…`

~~~~text
37: PHASE FCC_A1 % 2 1 1 !
38: CONST FCC_A1 : TH : VA : !
~~~~

[ThO-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-18Ber.tdb): FCC_A1, type code %, sha256 `7787fa4553bd2bc8…`

~~~~text
42: PHASE FCC_A1 % 2 1 1 !
43: CONST FCC_A1 : TH : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2018.09.013](https://doi.org/10.1016/j.jnucmat.2018.09.013) A. Bergeron, D. Manara, O. Beneš, R. Eloirdi, M.H.A. Piro, E.C. Corcoran, Thermodynamic modelling of thoria-urania and thoria-plutonia fuels: Description of the Th-U-Pu-O quaternary system, Journal of Nuclear Materials 512, 324-348 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0021-9614(03)00002-8](https://doi.org/10.1016/S0021-9614%2803%2900002-8) H. Kinoshita, D. Setoyama, Y. Saito, M. Hirota, K. Kurosaki, M. Uno, S. Yamanaka, J. Chem. Thermodyn., 35, 719-31(2003).  
_assessment that models this phase_

## ION (O–Th)

- Id: `phase:o-th:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2006.45–4000 K, x(O) 0–0.67229
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-th:ion)

Names (3): _corpus: _corpus:phase:o-th:ion  
_tdb: _tdb:ThO-03Kin.tdb:ION, tdb:ThO-18Ber.tdb:ION  


### TDB models of ION (2): PHASE and CONSTITUENT statements as written

[ThO-03Kin.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-03Kin.tdb): ION, type code %, sha256 `640414db2a764520…`

~~~~text
29: PHASE ION:Y % 2 1 1 !
30: CONST ION:Y : TH+4 : O-2 VA O : !
~~~~

[ThO-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-18Ber.tdb): ION, type code %, sha256 `7787fa4553bd2bc8…`

~~~~text
34: PHASE ION:Y % 2 1 1 !
35: CONST ION:Y : TH+4 : O-2 VA O : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2018.09.013](https://doi.org/10.1016/j.jnucmat.2018.09.013) A. Bergeron, D. Manara, O. Beneš, R. Eloirdi, M.H.A. Piro, E.C. Corcoran, Thermodynamic modelling of thoria-urania and thoria-plutonia fuels: Description of the Th-U-Pu-O quaternary system, Journal of Nuclear Materials 512, 324-348 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0021-9614(03)00002-8](https://doi.org/10.1016/S0021-9614%2803%2900002-8) H. Kinoshita, D. Setoyama, Y. Saito, M. Hirota, K. Kurosaki, M. Uno, S. Yamanaka, J. Chem. Thermodyn., 35, 719-31(2003).  
_assessment that models this phase_

## LIQUID (O–Th)

- Id: `phase:o-th:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Th 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-th:liquid)

Names (4): _corpus: _corpus:phase:o-th:liquid  
_paper: _paper:10.1016/j.jnucmat.2018.09.013:liquid  
_tdb: _tdb:ThO-03Kin.tdb:LIQUID, tdb:ThO-18Ber.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ThO-03Kin.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-03Kin.tdb): LIQUID, type code %, sha256 `640414db2a764520…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : TH : !
~~~~

[ThO-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-18Ber.tdb): LIQUID, type code %, sha256 `7787fa4553bd2bc8…`

~~~~text
37: PHASE LIQUID:L % 1 1 !
38: CONST LIQUID:L : TH : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2018.09.013](https://doi.org/10.1016/j.jnucmat.2018.09.013) A. Bergeron, D. Manara, O. Beneš, R. Eloirdi, M.H.A. Piro, E.C. Corcoran, Thermodynamic modelling of thoria-urania and thoria-plutonia fuels: Description of the Th-U-Pu-O quaternary system, Journal of Nuclear Materials 512, 324-348 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0021-9614(03)00002-8](https://doi.org/10.1016/S0021-9614%2803%2900002-8) H. Kinoshita, D. Setoyama, Y. Saito, M. Hirota, K. Kurosaki, M. Uno, S. Yamanaka, J. Chem. Thermodyn., 35, 719-31(2003).  
_assessment that models this phase_

## O2GAS (O–Th)

- Id: `phase:o-th:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-th:o2gas)

Names (3): _corpus: _corpus:phase:o-th:o2gas  
_tdb: _tdb:ThO-03Kin.tdb:O2GAS, tdb:ThO-18Ber.tdb:O2GAS  


### TDB models of O2GAS (2): PHASE and CONSTITUENT statements as written

[ThO-03Kin.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-03Kin.tdb): O2GAS, type code %, sha256 `640414db2a764520…`

~~~~text
50: PHASE O2GAS % 1 1 !
51: CONST O2GAS : O2 :!
~~~~

[ThO-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-18Ber.tdb): O2GAS, type code %, sha256 `7787fa4553bd2bc8…`

~~~~text
55: PHASE O2GAS % 1 1 !
56: CONST O2GAS : O2 :!
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2018.09.013](https://doi.org/10.1016/j.jnucmat.2018.09.013) A. Bergeron, D. Manara, O. Beneš, R. Eloirdi, M.H.A. Piro, E.C. Corcoran, Thermodynamic modelling of thoria-urania and thoria-plutonia fuels: Description of the Th-U-Pu-O quaternary system, Journal of Nuclear Materials 512, 324-348 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0021-9614(03)00002-8](https://doi.org/10.1016/S0021-9614%2803%2900002-8) H. Kinoshita, D. Setoyama, Y. Saito, M. Hirota, K. Kurosaki, M. Uno, S. Yamanaka, J. Chem. Thermodyn., 35, 719-31(2003).  
_assessment that models this phase_

## THO2_C1 (O–Th)

- Id: `phase:o-th:tho2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3680.2 K, x(O) 0.65904–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:o-th:tho2-c1)

Names (3): _corpus: _corpus:phase:o-th:tho2-c1  
_tdb: _tdb:ThO-03Kin.tdb:THO2_C1, tdb:ThO-18Ber.tdb:THO2_C1  


### TDB models of THO2_C1 (2): PHASE and CONSTITUENT statements as written

[ThO-03Kin.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-03Kin.tdb): THO2_C1, type code %, sha256 `640414db2a764520…`

~~~~text
47: PHASE THO2_C1 % 2 1 2 !
48: CONST THO2_C1 : TH : O% VA : !
~~~~

[ThO-18Ber.tdb](https://orchid-project.org/data/databases/sgte-binary/ThO-18Ber.tdb): THO2_C1, type code %, sha256 `7787fa4553bd2bc8…`

~~~~text
52: PHASE THO2_C1:I % 3 1 2 1 !
53: CONST THO2_C1:I : TH+3 TH+4% : O-2% VA : O-2 VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2018.09.013](https://doi.org/10.1016/j.jnucmat.2018.09.013) A. Bergeron, D. Manara, O. Beneš, R. Eloirdi, M.H.A. Piro, E.C. Corcoran, Thermodynamic modelling of thoria-urania and thoria-plutonia fuels: Description of the Th-U-Pu-O quaternary system, Journal of Nuclear Materials 512, 324-348 (2018).  
_assessment that models this phase_
- [doi:10.1016/S0021-9614(03)00002-8](https://doi.org/10.1016/S0021-9614%2803%2900002-8) H. Kinoshita, D. Setoyama, Y. Saito, M. Hirota, K. Kurosaki, M. Uno, S. Yamanaka, J. Chem. Thermodyn., 35, 719-31(2003).  
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
