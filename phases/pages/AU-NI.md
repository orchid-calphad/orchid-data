# Au–Ni phases

> Au–Ni system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-NI.html · Markdown: https://data.orchid-project.org/phases/pages/AU-NI.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-NI) · [full JSON](https://data.orchid-project.org/phases/systems/AU-NI.json) · [Au–Ni system page](https://data.orchid-project.org/systems/AU-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Ni system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-au-ni-bcc-a2); _phase:au-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-au-ni-fcc-a1); _phase:au-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499.49 K, x(Ni) 0–1 | 3 | 3 |
| [HCP_A3](#phase-au-ni-hcp-a3); _phase:au-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-au-ni-liquid); _phase:au-ni:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1214.36–2500 K, x(Ni) 0–1 | 3 | 3 |

## BCC_A2 (Au–Ni)

- Id: `phase:au-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ni:bcc-a2)

Names (4): _corpus: _corpus:phase:au-ni:bcc-a2  
_tdb: _tdb:AuNi-05Fra.tdb:BCC_A2, tdb:AuNi-05Wan-LB.tdb:BCC_A2, tdb:AuNi-99Mor.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AuNi-05Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-05Fra.tdb): BCC_A2, type code %B, sha256 `4fddd1656b2b994e…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU NI : VA : !
~~~~

[AuNi-05Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-05Wan-LB.tdb): BCC_A2, type code %B, sha256 `5b08e4a5043680ac…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU NI : VA : !
~~~~

[AuNi-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-99Mor.tdb): BCC_A2, type code %B, sha256 `2c3f71de4250cebd…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.09.004](https://doi.org/10.1016/j.calphad.2005.09.004) Jianhua Wang, Xiao-Gang Lu, Bo Sundman, Xuping Su, Thermodynamic assessment of the Au–Ni system, Calphad 29, 263-268 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase_

## FCC_A1 (Au–Ni)

- Id: `phase:au-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499.49 K, x(Ni) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ni:fcc-a1)

Names (5): _corpus: _corpus:phase:au-ni:fcc-a1  
_paper: _paper:10.1361/105497199770335785:fcc  
_tdb: _tdb:AuNi-05Fra.tdb:FCC_A1, tdb:AuNi-05Wan-LB.tdb:FCC_A1, tdb:AuNi-99Mor.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AuNi-05Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-05Fra.tdb): FCC_A1, type code %A, sha256 `4fddd1656b2b994e…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU% NI% : VA : !
~~~~

[AuNi-05Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-05Wan-LB.tdb): FCC_A1, type code %A, sha256 `5b08e4a5043680ac…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU% NI% : VA : !
~~~~

[AuNi-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-99Mor.tdb): FCC_A1, type code %A, sha256 `2c3f71de4250cebd…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU% NI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.09.004](https://doi.org/10.1016/j.calphad.2005.09.004) Jianhua Wang, Xiao-Gang Lu, Bo Sundman, Xuping Su, Thermodynamic assessment of the Au–Ni system, Calphad 29, 263-268 (2005).  
_assessment that models this phase_

## HCP_A3 (Au–Ni)

- Id: `phase:au-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ni:hcp-a3)

Names (4): _corpus: _corpus:phase:au-ni:hcp-a3  
_tdb: _tdb:AuNi-05Fra.tdb:HCP_A3, tdb:AuNi-05Wan-LB.tdb:HCP_A3, tdb:AuNi-99Mor.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AuNi-05Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-05Fra.tdb): HCP_A3, type code %A, sha256 `4fddd1656b2b994e…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU NI : VA : !
~~~~

[AuNi-05Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-05Wan-LB.tdb): HCP_A3, type code %A, sha256 `5b08e4a5043680ac…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU NI : VA : !
~~~~

[AuNi-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-99Mor.tdb): HCP_A3, type code %A, sha256 `2c3f71de4250cebd…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.09.004](https://doi.org/10.1016/j.calphad.2005.09.004) Jianhua Wang, Xiao-Gang Lu, Bo Sundman, Xuping Su, Thermodynamic assessment of the Au–Ni system, Calphad 29, 263-268 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase_

## LIQUID (Au–Ni)

- Id: `phase:au-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1214.36–2500 K, x(Ni) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ni:liquid)

Names (5): _corpus: _corpus:phase:au-ni:liquid  
_paper: _paper:10.1361/105497199770335785:Liquid  
_tdb: _tdb:AuNi-05Fra.tdb:LIQUID, tdb:AuNi-05Wan-LB.tdb:LIQUID, tdb:AuNi-99Mor.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AuNi-05Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-05Fra.tdb): LIQUID, type code %, sha256 `4fddd1656b2b994e…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU NI : !
~~~~

[AuNi-05Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-05Wan-LB.tdb): LIQUID, type code %, sha256 `5b08e4a5043680ac…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU NI : !
~~~~

[AuNi-99Mor.tdb](https://orchid-project.org/data/databases/sgte-binary/AuNi-99Mor.tdb): LIQUID, type code %, sha256 `2c3f71de4250cebd…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497199770335785](https://doi.org/10.1361/105497199770335785) S. Morioka, M. Hasebe, Thermodynamic constraints to describe gibbs energies for binary alloys, JPE 20, 244-257 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2005.09.004](https://doi.org/10.1016/j.calphad.2005.09.004) Jianhua Wang, Xiao-Gang Lu, Bo Sundman, Xuping Su, Thermodynamic assessment of the Au–Ni system, Calphad 29, 263-268 (2005).  
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
