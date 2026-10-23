# Sm–Ti phases

> Sm–Ti system: 5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SM-TI.html · Markdown: https://data.orchid-project.org/phases/pages/SM-TI.md

5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SM-TI) · [full JSON](https://data.orchid-project.org/phases/systems/SM-TI.json) · [Sm–Ti system page](https://data.orchid-project.org/systems/SM-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/SM-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sm–Ti system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-sm-ti-bcc-a2); _phase:sm-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1146.55–2499.73 K, x(Ti) 0–1 | 4 | 1 |
| [FCC_A1](#phase-sm-ti-fcc-a1); _phase:sm-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1150–1150 K, x(Ti) 0.24–0.92 | 0 | 1 |
| [HCP_A3](#phase-sm-ti-hcp-a3); _phase:sm-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1931.55 K, x(Ti) 0–1 | 3 | 1 |
| [LIQUID](#phase-sm-ti-liquid); _phase:sm-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1309.39–2500 K, x(Ti) 0–1 | 2 | 1 |
| [RHOMB_C19](#phase-sm-ti-rhomb-c19); _phase:sm-ti:rhomb-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1150 K, x(Ti) 0–0.9 | 1 | 1 |

## BCC_A2 (Sm–Ti)

- Id: `phase:sm-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1146.55–2499.73 K, x(Ti) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sm-ti:bcc-a2)

Names (4): _corpus: _corpus:phase:sm-ti:bcc-a2  
_paper: _paper:10.1016/j.calphad.2021.102357:bcc, paper:10.1016/j.calphad.2021.102357:bcc#2  
_tdb: _tdb:SmTi-21Sae.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SmTi-21Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/SmTi-21Sae.tdb): BCC_A2, type code %B, sha256 `d33873229a2fab02…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : SM TI% : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102357](https://doi.org/10.1016/j.calphad.2021.102357) Arkapol Saengdeejing, Ying Chen, Osamu Takeda, Masanori Enoki, Satoshi Sugimoto, Hiroshi Ohtani et al., Sm–Ti binary thermodynamic database and phase diagram, Calphad 75, 102357 (2021).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Sm–Ti)

- Id: `phase:sm-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1150–1150 K, x(Ti) 0.24–0.92
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sm-ti:fcc-a1)

Names (2): _corpus: _corpus:phase:sm-ti:fcc-a1  
_tdb: _tdb:SmTi-21Sae.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SmTi-21Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/SmTi-21Sae.tdb): FCC_A1, type code %A, sha256 `d33873229a2fab02…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : SM TI : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102357](https://doi.org/10.1016/j.calphad.2021.102357) Arkapol Saengdeejing, Ying Chen, Osamu Takeda, Masanori Enoki, Satoshi Sugimoto, Hiroshi Ohtani et al., Sm–Ti binary thermodynamic database and phase diagram, Calphad 75, 102357 (2021).  
_assessment that models this phase_

## HCP_A3 (Sm–Ti)

- Id: `phase:sm-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1931.55 K, x(Ti) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sm-ti:hcp-a3)

Names (4): _corpus: _corpus:phase:sm-ti:hcp-a3  
_paper: _paper:10.1016/j.calphad.2021.102357:hcp, paper:10.1016/j.calphad.2021.102357:hcp#2  
_tdb: _tdb:SmTi-21Sae.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SmTi-21Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/SmTi-21Sae.tdb): HCP_A3, type code %A, sha256 `d33873229a2fab02…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : SM TI% : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102357](https://doi.org/10.1016/j.calphad.2021.102357) Arkapol Saengdeejing, Ying Chen, Osamu Takeda, Masanori Enoki, Satoshi Sugimoto, Hiroshi Ohtani et al., Sm–Ti binary thermodynamic database and phase diagram, Calphad 75, 102357 (2021).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Sm–Ti)

- Id: `phase:sm-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1309.39–2500 K, x(Ti) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sm-ti:liquid)

Names (3): _corpus: _corpus:phase:sm-ti:liquid  
_paper: _paper:10.1016/j.calphad.2021.102357:Liquid  
_tdb: _tdb:SmTi-21Sae.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SmTi-21Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/SmTi-21Sae.tdb): LIQUID, type code %, sha256 `d33873229a2fab02…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : SM TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102357](https://doi.org/10.1016/j.calphad.2021.102357) Arkapol Saengdeejing, Ying Chen, Osamu Takeda, Masanori Enoki, Satoshi Sugimoto, Hiroshi Ohtani et al., Sm–Ti binary thermodynamic database and phase diagram, Calphad 75, 102357 (2021).  
_assessment that models this phase; reports values for this phase_

## RHOMB_C19 (Sm–Ti)

- Id: `phase:sm-ti:rhomb-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1150 K, x(Ti) 0–0.9
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sm-ti:rhomb-c19)

Names (3): _corpus: _corpus:phase:sm-ti:rhomb-c19  
_paper: _paper:10.1016/j.calphad.2021.102357:Rhombohedral  
_tdb: _tdb:SmTi-21Sae.tdb:RHOMB_C19  


### TDB models of RHOMB_C19 (1): PHASE and CONSTITUENT statements as written

[SmTi-21Sae.tdb](https://orchid-project.org/data/databases/sgte-binary/SmTi-21Sae.tdb): RHOMB_C19, type code %, sha256 `d33873229a2fab02…`

~~~~text
42: PHASE RHOMB_C19 % 1 1 !
43: CONST RHOMB_C19 : SM% TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102357](https://doi.org/10.1016/j.calphad.2021.102357) Arkapol Saengdeejing, Ying Chen, Osamu Takeda, Masanori Enoki, Satoshi Sugimoto, Hiroshi Ohtani et al., Sm–Ti binary thermodynamic database and phase diagram, Calphad 75, 102357 (2021).  
_assessment that models this phase; reports values for this phase_

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
