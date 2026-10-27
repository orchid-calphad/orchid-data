# Ho–Mo phases

> Ho–Mo system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HO-MO.html · Markdown: https://data.orchid-project.org/phases/pages/HO-MO.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HO-MO) · [full JSON](https://data.orchid-project.org/phases/systems/HO-MO.json) · [Ho–Mo system page](https://data.orchid-project.org/systems/HO-MO.html) · [Markdown](https://data.orchid-project.org/phases/pages/HO-MO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ho–Mo system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ho-mo-bcc-a2); _phase:ho-mo:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.74 K, x(Mo) 0–1 | 4 | 2 |
| [FCC_A1](#phase-ho-mo-fcc-a1); _phase:ho-mo:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ho-mo-hcp-a3); _phase:ho-mo:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1747 K, x(Mo) 0–0.01021 | 2 | 2 |
| [LIQUID](#phase-ho-mo-liquid); _phase:ho-mo:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1705.04–4000 K, x(Mo) 0–1 | 4 | 2 |

## BCC_A2 (Ho–Mo)

- Id: `phase:ho-mo:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.74 K, x(Mo) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mo:bcc-a2)

Names (4): _corpus: _corpus:phase:ho-mo:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2009.08.042:(Mo)  
_tdb: _tdb:HoMo-09Wan-newHo.tdb:BCC_A2, tdb:HoMo-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HoMo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan-newHo.tdb): BCC_A2, type code %B, sha256 `2cb4d1dc467d9eae…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : HO MO% : VA : !
~~~~

[HoMo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan.tdb): BCC_A2, type code %B, sha256 `7b0eef23feb49676…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : HO MO% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ho–Mo)

- Id: `phase:ho-mo:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mo:fcc-a1)

Names (3): _corpus: _corpus:phase:ho-mo:fcc-a1  
_tdb: _tdb:HoMo-09Wan-newHo.tdb:FCC_A1, tdb:HoMo-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HoMo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan-newHo.tdb): FCC_A1, type code %A, sha256 `2cb4d1dc467d9eae…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : HO MO : VA : !
~~~~

[HoMo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan.tdb): FCC_A1, type code %A, sha256 `7b0eef23feb49676…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : HO MO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase_

## HCP_A3 (Ho–Mo)

- Id: `phase:ho-mo:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1747 K, x(Mo) 0–0.01021
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mo:hcp-a3)

Names (4): _corpus: _corpus:phase:ho-mo:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.08.042:(Ho)  
_tdb: _tdb:HoMo-09Wan-newHo.tdb:HCP_A3, tdb:HoMo-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HoMo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan-newHo.tdb): HCP_A3, type code %A, sha256 `2cb4d1dc467d9eae…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : HO% MO : VA : !
~~~~

[HoMo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan.tdb): HCP_A3, type code %A, sha256 `7b0eef23feb49676…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : HO% MO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ho–Mo)

- Id: `phase:ho-mo:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1705.04–4000 K, x(Mo) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-mo:liquid)

Names (5): _corpus: _corpus:phase:ho-mo:liquid  
_paper: _paper:10.1016/j.jallcom.2009.08.042:L, paper:10.1016/j.jallcom.2009.08.042:L1  
_tdb: _tdb:HoMo-09Wan-newHo.tdb:LIQUID, tdb:HoMo-09Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HoMo-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan-newHo.tdb): LIQUID, type code %, sha256 `2cb4d1dc467d9eae…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : HO MO : !
~~~~

[HoMo-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoMo-09Wan.tdb): LIQUID, type code %, sha256 `7b0eef23feb49676…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : HO MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
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
