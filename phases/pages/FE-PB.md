# Fe–Pb phases

> Fe–Pb system: 5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-PB.html · Markdown: https://data.orchid-project.org/phases/pages/FE-PB.md

5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-PB) · [full JSON](https://data.orchid-project.org/phases/systems/FE-PB.json) · [Fe–Pb system page](https://data.orchid-project.org/systems/FE-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Pb system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-pb-bcc-a2); _phase:fe-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1824.58 K, x(Pb) 0–2e-05 | 11 | 2 |
| [FCC_A1](#phase-fe-pb-fcc-a1); _phase:fe-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1667.49 K, x(Pb) 0–1 | 9 | 2 |
| [GAS](#phase-fe-pb-gas); _phase:fe-pb:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 2019.02–2500 K, x(Pb) 0.96684–1 | 0 | 1 |
| [HCP_A3](#phase-fe-pb-hcp-a3); _phase:fe-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-fe-pb-liquid); _phase:fe-pb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 300.62–2500 K, x(Pb) 0–1 | 11 | 2 |

## BCC_A2 (Fe–Pb)

- Id: `phase:fe-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1824.58 K, x(Pb) 0–2e-05
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pb:bcc-a2)

Names (4): _corpus: _corpus:phase:fe-pb:bcc-a2  
_paper: _paper:10.1016/j.tca.2011.06.014:bcc  
_tdb: _tdb:FePb-11Vaa.tdb:BCC_A2, tdb:FePb-87Din-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[FePb-11Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-11Vaa.tdb): BCC_A2, type code %B, sha256 `05c82ebb8d79a2c2…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : FE PB : VA : !
~~~~

[FePb-87Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-87Din-LB.tdb): BCC_A2, type code %B, sha256 `b26c9577ad72412f…`

~~~~text
48: PHASE BCC_A2 %B 2 1 3 !
49: CONST BCC_A2 : FE PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2011.06.014](https://doi.org/10.1016/j.tca.2011.06.014) I. Vaajamo, P. Taskinen, A thermodynamic assessment of the iron–lead binary system, Thermochimica Acta 524, 56-61 (2011).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Fe–Pb)

- Id: `phase:fe-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1667.49 K, x(Pb) 0–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pb:fcc-a1)

Names (4): _corpus: _corpus:phase:fe-pb:fcc-a1  
_paper: _paper:10.1016/j.tca.2011.06.014:fcc  
_tdb: _tdb:FePb-11Vaa.tdb:FCC_A1, tdb:FePb-87Din-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[FePb-11Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-11Vaa.tdb): FCC_A1, type code %A, sha256 `05c82ebb8d79a2c2…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : FE PB : VA : !
~~~~

[FePb-87Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-87Din-LB.tdb): FCC_A1, type code %A, sha256 `b26c9577ad72412f…`

~~~~text
43: PHASE FCC_A1 %A 2 1 1 !
44: CONST FCC_A1 : FE PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2011.06.014](https://doi.org/10.1016/j.tca.2011.06.014) I. Vaajamo, P. Taskinen, A thermodynamic assessment of the iron–lead binary system, Thermochimica Acta 524, 56-61 (2011).  
_assessment that models this phase; reports values for this phase_

## GAS (Fe–Pb)

- Id: `phase:fe-pb:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2019.02–2500 K, x(Pb) 0.96684–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pb:gas)

Names (2): _corpus: _corpus:phase:fe-pb:gas  
_tdb: _tdb:FePb-87Din-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[FePb-87Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-87Din-LB.tdb): GAS, type code %, sha256 `b26c9577ad72412f…`

~~~~text
56: PHASE GAS:G % 1 1 !
57: CONST GAS:G : FE FE2 PB PB2 : !
~~~~

## HCP_A3 (Fe–Pb)

- Id: `phase:fe-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pb:hcp-a3)

Names (3): _corpus: _corpus:phase:fe-pb:hcp-a3  
_tdb: _tdb:FePb-11Vaa.tdb:HCP_A3, tdb:FePb-87Din-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[FePb-11Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-11Vaa.tdb): HCP_A3, type code %, sha256 `05c82ebb8d79a2c2…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : FE PB : VA : !
~~~~

[FePb-87Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-87Din-LB.tdb): HCP_A3, type code %, sha256 `b26c9577ad72412f…`

~~~~text
53: PHASE HCP_A3 % 2 1 0.5 !
54: CONST HCP_A3 : FE PB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2011.06.014](https://doi.org/10.1016/j.tca.2011.06.014) I. Vaajamo, P. Taskinen, A thermodynamic assessment of the iron–lead binary system, Thermochimica Acta 524, 56-61 (2011).  
_assessment that models this phase_

## LIQUID (Fe–Pb)

- Id: `phase:fe-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.62–2500 K, x(Pb) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pb:liquid)

Names (5): _corpus: _corpus:phase:fe-pb:liquid  
_paper: _paper:10.1016/j.tca.2011.06.014:L1, paper:10.1016/j.tca.2011.06.014:L2  
_tdb: _tdb:FePb-11Vaa.tdb:LIQUID, tdb:FePb-87Din-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[FePb-11Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-11Vaa.tdb): LIQUID, type code %, sha256 `05c82ebb8d79a2c2…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : FE PB : !
~~~~

[FePb-87Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePb-87Din-LB.tdb): LIQUID, type code %, sha256 `b26c9577ad72412f…`

~~~~text
38: PHASE LIQUID:L % 1 1 !
39: CONST LIQUID:L : FE PB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2011.06.014](https://doi.org/10.1016/j.tca.2011.06.014) I. Vaajamo, P. Taskinen, A thermodynamic assessment of the iron–lead binary system, Thermochimica Acta 524, 56-61 (2011).  
_assessment that models this phase; reports values for this phase_

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
