# Ho–V phases

> Ho–V system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HO-V.html · Markdown: https://data.orchid-project.org/phases/pages/HO-V.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HO-V) · [full JSON](https://data.orchid-project.org/phases/systems/HO-V.json) · [Ho–V system page](https://data.orchid-project.org/systems/HO-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/HO-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ho–V system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ho-v-bcc-a2); _phase:ho-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.24 K, x(V) 0–1 | 4 | 2 |
| [FCC_A1](#phase-ho-v-fcc-a1); _phase:ho-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ho-v-hcp-a3); _phase:ho-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1748 K, x(V) 0–0.00571 | 2 | 2 |
| [LIQUID](#phase-ho-v-liquid); _phase:ho-v:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1702.55–4000 K, x(V) 0–1 | 4 | 2 |

## BCC_A2 (Ho–V)

- Id: `phase:ho-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.24 K, x(V) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-v:bcc-a2)

Names (4): _corpus: _corpus:phase:ho-v:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2009.08.042:(V)  
_tdb: _tdb:HoV-09Wan-newHo.tdb:BCC_A2, tdb:HoV-09Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HoV-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan-newHo.tdb): BCC_A2, type code %B, sha256 `930e37db75afc59b…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : HO V% : VA : !
~~~~

[HoV-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan.tdb): BCC_A2, type code %B, sha256 `fc4a88833a46ac6a…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : HO V% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ho–V)

- Id: `phase:ho-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-v:fcc-a1)

Names (3): _corpus: _corpus:phase:ho-v:fcc-a1  
_tdb: _tdb:HoV-09Wan-newHo.tdb:FCC_A1, tdb:HoV-09Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HoV-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan-newHo.tdb): FCC_A1, type code %A, sha256 `930e37db75afc59b…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : HO V : VA : !
~~~~

[HoV-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan.tdb): FCC_A1, type code %A, sha256 `fc4a88833a46ac6a…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : HO V : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase_

## HCP_A3 (Ho–V)

- Id: `phase:ho-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1748 K, x(V) 0–0.00571
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-v:hcp-a3)

Names (4): _corpus: _corpus:phase:ho-v:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2009.08.042:(Ho)  
_tdb: _tdb:HoV-09Wan-newHo.tdb:HCP_A3, tdb:HoV-09Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HoV-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan-newHo.tdb): HCP_A3, type code %A, sha256 `930e37db75afc59b…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : HO% V : VA : !
~~~~

[HoV-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan.tdb): HCP_A3, type code %A, sha256 `fc4a88833a46ac6a…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : HO% V : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ho–V)

- Id: `phase:ho-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1702.55–4000 K, x(V) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ho-v:liquid)

Names (5): _corpus: _corpus:phase:ho-v:liquid  
_paper: _paper:10.1016/j.jallcom.2009.08.042:L, paper:10.1016/j.jallcom.2009.08.042:L1  
_tdb: _tdb:HoV-09Wan-newHo.tdb:LIQUID, tdb:HoV-09Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HoV-09Wan-newHo.tdb](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan-newHo.tdb): LIQUID, type code %, sha256 `930e37db75afc59b…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : HO V : !
~~~~

[HoV-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/HoV-09Wan.tdb): LIQUID, type code %, sha256 `fc4a88833a46ac6a…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : HO V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2009.08.042](https://doi.org/10.1016/j.jallcom.2009.08.042) C.P. Wang, S.H. Guo, X.J. Liu, A.T. Tang, F.S. Pan, Thermodynamic assessments of the Ho–X (X: Cu, Mo, V) systems, Journal of Alloys and Compounds 487, 173-178 (2009).  
_assessment that models this phase; reports values for this phase_

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
