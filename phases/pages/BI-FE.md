# Bi–Fe phases

> Bi–Fe system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-FE.html · Markdown: https://data.orchid-project.org/phases/pages/BI-FE.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-FE) · [full JSON](https://data.orchid-project.org/phases/systems/BI-FE.json) · [Bi–Fe system page](https://data.orchid-project.org/systems/BI-FE.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-FE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Fe system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-fe-a7-rhombohedral); _phase:bi-fe:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.68 K, x(Fe) 0–0.00058 | 2 | 1 |
| [BCC_A2](#phase-bi-fe-bcc-a2); _phase:bi-fe:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1810.95 K, x(Fe) 0.97692–1 | 5 | 1 |
| [FCC_A1](#phase-bi-fe-fcc-a1); _phase:bi-fe:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1182.57–1667.47 K, x(Fe) 0.98199–1 | 2 | 1 |
| [HCP_A3](#phase-bi-fe-hcp-a3); _phase:bi-fe:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-bi-fe-liquid); _phase:bi-fe:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 544.68–2500 K, x(Fe) 0–1 | 5 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Fe)

- Id: `phase:bi-fe:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.68 K, x(Fe) 0–0.00058
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-fe:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-fe:a7-rhombohedral, corpus:phase:bi-fe:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2008.01.001:(Bi)  
_tdb: _tdb:BiFe-08Boa.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiFe-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/BiFe-08Boa.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `140bebc3aabbbff0…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI% FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Bi–Fe)

- Id: `phase:bi-fe:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1810.95 K, x(Fe) 0.97692–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-fe:bcc-a2)

Names (4): _corpus: _corpus:phase:bi-fe:bcc-a2  
_paper: _paper:10.1016/j.calphad.2008.01.001:αFe, paper:10.1016/j.calphad.2008.01.001:δFe  
_tdb: _tdb:BiFe-08Boa.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiFe-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/BiFe-08Boa.tdb): BCC_A2, type code %B, sha256 `140bebc3aabbbff0…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BI FE% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Bi–Fe)

- Id: `phase:bi-fe:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1182.57–1667.47 K, x(Fe) 0.98199–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-fe:fcc-a1)

Names (3): _corpus: _corpus:phase:bi-fe:fcc-a1  
_paper: _paper:10.1016/j.calphad.2008.01.001:γFe  
_tdb: _tdb:BiFe-08Boa.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiFe-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/BiFe-08Boa.tdb): FCC_A1, type code %A, sha256 `140bebc3aabbbff0…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BI FE% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Bi–Fe)

- Id: `phase:bi-fe:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-fe:hcp-a3)

Names (2): _corpus: _corpus:phase:bi-fe:hcp-a3  
_tdb: _tdb:BiFe-08Boa.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiFe-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/BiFe-08Boa.tdb): HCP_A3, type code %A, sha256 `140bebc3aabbbff0…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BI FE : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
_assessment that models this phase_

## LIQUID (Bi–Fe)

- Id: `phase:bi-fe:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 544.68–2500 K, x(Fe) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-fe:liquid)

Names (3): _corpus: _corpus:phase:bi-fe:liquid  
_paper: _paper:10.1016/j.calphad.2008.01.001:L1  
_tdb: _tdb:BiFe-08Boa.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiFe-08Boa.tdb](https://orchid-project.org/data/databases/sgte-binary/BiFe-08Boa.tdb): LIQUID, type code %, sha256 `140bebc3aabbbff0…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BI FE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.01.001](https://doi.org/10.1016/j.calphad.2008.01.001) D. Boa, S. Hassam, G. Kra, K.P. Kotchi, J. Rogez, The ternary bismuth–iron–antimony system: Experimental phase diagram study and thermodynamic evaluation, Calphad 32, 227-239 (2008).  
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
