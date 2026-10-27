# Dy–Er phases

> Dy–Er system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/DY-ER.html · Markdown: https://data.orchid-project.org/phases/pages/DY-ER.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=DY-ER) · [full JSON](https://data.orchid-project.org/phases/systems/DY-ER.json) · [Dy–Er system page](https://data.orchid-project.org/systems/DY-ER.html) · [Markdown](https://data.orchid-project.org/phases/pages/DY-ER.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Dy–Er system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-dy-er-bcc-a2); _phase:dy-er:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1654.15–1742.9 K, x(Er) 0–0.4969 | 0 | 1 |
| [FCC_A1](#phase-dy-er-fcc-a1); _phase:dy-er:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-dy-er-hcp-a3); _phase:dy-er:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1802 K, x(Er) 0–1 | 0 | 1 |
| [LIQUID](#phase-dy-er-liquid); _phase:dy-er:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1685.11–2500 K, x(Er) 0–1 | 0 | 1 |

## BCC_A2 (Dy–Er)

- Id: `phase:dy-er:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1654.15–1742.9 K, x(Er) 0–0.4969
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-er:bcc-a2)

Names (2): _corpus: _corpus:phase:dy-er:bcc-a2  
_tdb: _tdb:DyEr-00Nor-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[DyEr-00Nor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyEr-00Nor-LB.tdb): BCC_A2, type code %B, sha256 `d9b5e4d4e906631a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : DY ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497100770340200](https://doi.org/10.1361/105497100770340200) Susanne Norgren, Thermodynamic assessment of the Ho-Tb, Ho-Dy, Ho-Er, Er-Tb, and Er-Dy systems, JPE 21, 148-156 (2000).  
_assessment that models this phase_

## FCC_A1 (Dy–Er)

- Id: `phase:dy-er:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-er:fcc-a1)

Names (2): _corpus: _corpus:phase:dy-er:fcc-a1  
_tdb: _tdb:DyEr-00Nor-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[DyEr-00Nor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyEr-00Nor-LB.tdb): FCC_A1, type code %A, sha256 `d9b5e4d4e906631a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : DY ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497100770340200](https://doi.org/10.1361/105497100770340200) Susanne Norgren, Thermodynamic assessment of the Ho-Tb, Ho-Dy, Ho-Er, Er-Tb, and Er-Dy systems, JPE 21, 148-156 (2000).  
_assessment that models this phase_

## HCP_A3 (Dy–Er)

- Id: `phase:dy-er:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1802 K, x(Er) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-er:hcp-a3)

Names (2): _corpus: _corpus:phase:dy-er:hcp-a3  
_tdb: _tdb:DyEr-00Nor-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[DyEr-00Nor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyEr-00Nor-LB.tdb): HCP_A3, type code %A, sha256 `d9b5e4d4e906631a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : DY ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497100770340200](https://doi.org/10.1361/105497100770340200) Susanne Norgren, Thermodynamic assessment of the Ho-Tb, Ho-Dy, Ho-Er, Er-Tb, and Er-Dy systems, JPE 21, 148-156 (2000).  
_assessment that models this phase_

## LIQUID (Dy–Er)

- Id: `phase:dy-er:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1685.11–2500 K, x(Er) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:dy-er:liquid)

Names (2): _corpus: _corpus:phase:dy-er:liquid  
_tdb: _tdb:DyEr-00Nor-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[DyEr-00Nor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/DyEr-00Nor-LB.tdb): LIQUID, type code %, sha256 `d9b5e4d4e906631a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : DY ER : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497100770340200](https://doi.org/10.1361/105497100770340200) Susanne Norgren, Thermodynamic assessment of the Ho-Tb, Ho-Dy, Ho-Er, Er-Tb, and Er-Dy systems, JPE 21, 148-156 (2000).  
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
