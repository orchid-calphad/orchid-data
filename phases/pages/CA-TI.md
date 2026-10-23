# Ca–Ti phases

> Ca–Ti system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-TI.html · Markdown: https://data.orchid-project.org/phases/pages/CA-TI.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-TI) · [full JSON](https://data.orchid-project.org/phases/systems/CA-TI.json) · [Ca–Ti system page](https://data.orchid-project.org/systems/CA-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Ti system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-ti-bcc-a2); _phase:ca-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2145.98 K, x(Ti) 0–1 | 2 | 1 |
| [FCC_A1](#phase-ca-ti-fcc-a1); _phase:ca-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–716.03 K, x(Ti) 0–0 | 1 | 1 |
| [HCP_A3](#phase-ca-ti-hcp-a3); _phase:ca-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1156.02 K, x(Ti) 0.99953–1 | 4 | 1 |
| [LIQUID](#phase-ca-ti-liquid); _phase:ca-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1114.76–2500 K, x(Ti) 0–1 | 3 | 1 |

## BCC_A2 (Ca–Ti)

- Id: `phase:ca-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2145.98 K, x(Ti) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ti:bcc-a2)

Names (3): _corpus: _corpus:phase:ca-ti:bcc-a2  
_paper: _paper:10.1007/s10853-015-9130-x:βCa  
_tdb: _tdb:CaTi-15Ham.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaTi-15Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaTi-15Ham.tdb): BCC_A2, type code %B, sha256 `3a0af4e503124843…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CA% TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-015-9130-x](https://doi.org/10.1007/s10853-015-9130-x) Milan Hampl, Rainer Schmid-Fetzer, Experimental investigation and thermodynamic assessment of the Al–Ca–Ti system, J Mater Sci 50, 5822-5832 (2015).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ca–Ti)

- Id: `phase:ca-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–716.03 K, x(Ti) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:ca-ti:fcc-a1  
_paper: _paper:10.1007/s10853-015-9130-x:αCa  
_tdb: _tdb:CaTi-15Ham.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaTi-15Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaTi-15Ham.tdb): FCC_A1, type code %A, sha256 `3a0af4e503124843…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CA% TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-015-9130-x](https://doi.org/10.1007/s10853-015-9130-x) Milan Hampl, Rainer Schmid-Fetzer, Experimental investigation and thermodynamic assessment of the Al–Ca–Ti system, J Mater Sci 50, 5822-5832 (2015).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ca–Ti)

- Id: `phase:ca-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1156.02 K, x(Ti) 0.99953–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ti:hcp-a3)

Names (4): _corpus: _corpus:phase:ca-ti:hcp-a3  
_paper: _paper:10.1007/s10853-015-9130-x:αTi, paper:10.1007/s10853-015-9130-x:βTi  
_tdb: _tdb:CaTi-15Ham.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaTi-15Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaTi-15Ham.tdb): HCP_A3, type code %A, sha256 `3a0af4e503124843…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CA TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-015-9130-x](https://doi.org/10.1007/s10853-015-9130-x) Milan Hampl, Rainer Schmid-Fetzer, Experimental investigation and thermodynamic assessment of the Al–Ca–Ti system, J Mater Sci 50, 5822-5832 (2015).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ca–Ti)

- Id: `phase:ca-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1114.76–2500 K, x(Ti) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ti:liquid)

Names (3): _corpus: _corpus:phase:ca-ti:liquid  
_paper: _paper:10.1007/s10853-015-9130-x:L'  
_tdb: _tdb:CaTi-15Ham.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaTi-15Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaTi-15Ham.tdb): LIQUID, type code %, sha256 `3a0af4e503124843…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CA TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s10853-015-9130-x](https://doi.org/10.1007/s10853-015-9130-x) Milan Hampl, Rainer Schmid-Fetzer, Experimental investigation and thermodynamic assessment of the Al–Ca–Ti system, J Mater Sci 50, 5822-5832 (2015).  
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
