# Li–Na phases

> Li–Na system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LI-NA.html · Markdown: https://data.orchid-project.org/phases/pages/LI-NA.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LI-NA) · [full JSON](https://data.orchid-project.org/phases/systems/LI-NA.json) · [Li–Na system page](https://data.orchid-project.org/systems/LI-NA.html) · [Markdown](https://data.orchid-project.org/phases/pages/LI-NA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Li–Na system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-li-na-bcc-a2); _phase:li-na:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–454.6 K, x(Na) 0–1 | 8 | 1 |
| [FCC_A1](#phase-li-na-fcc-a1); _phase:li-na:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-li-na-hcp-a3); _phase:li-na:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-li-na-liquid); _phase:li-na:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 360–2500 K, x(Na) 0–1 | 15 | 1 |

## BCC_A2 (Li–Na)

- Id: `phase:li-na:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–454.6 K, x(Na) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-na:bcc-a2)

Names (4): _corpus: _corpus:phase:li-na:bcc-a2  
_paper: _paper:10.1016/j.calphad.2003.09.001:bcc(Li), paper:10.1016/j.calphad.2003.09.001:bcc(Na)  
_tdb: _tdb:LiNa-03Zha-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LiNa-03Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiNa-03Zha-LB.tdb): BCC_A2, type code %B, sha256 `04ec75b2710df32a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : LI NA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001) Shengjun Zhang, Dongwon Shin, Zi-Kui Liu, Thermodynamic modeling of the Ca–Li–Na system, Calphad 27, 235-241 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1039/dt9750001490](https://doi.org/10.1039/dt9750001490) Michael G. Down, Peter Hubberstey, Richard J. Pulham, Sodium–lithium phase diagram: redetermination of the liquid immiscibility system by resistance measurement, J. Chem. Soc., Dalton Trans., 1490 (1975).  
_cited as the source of values for this phase_
- [doi:10.1021/j150535a004](https://doi.org/10.1021/j150535a004) O. N. Salmon, D. H. Ahmann, The Lithiuim–Sodium Liquid Metal System, J. Phys. Chem. 60, 13-14 (1956).  
_cited as the source of values for this phase_

## FCC_A1 (Li–Na)

- Id: `phase:li-na:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-na:fcc-a1)

Names (2): _corpus: _corpus:phase:li-na:fcc-a1  
_tdb: _tdb:LiNa-03Zha-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LiNa-03Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiNa-03Zha-LB.tdb): FCC_A1, type code %A, sha256 `04ec75b2710df32a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : LI NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001) Shengjun Zhang, Dongwon Shin, Zi-Kui Liu, Thermodynamic modeling of the Ca–Li–Na system, Calphad 27, 235-241 (2003).  
_assessment that models this phase_

## HCP_A3 (Li–Na)

- Id: `phase:li-na:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-na:hcp-a3)

Names (2): _corpus: _corpus:phase:li-na:hcp-a3  
_tdb: _tdb:LiNa-03Zha-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LiNa-03Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiNa-03Zha-LB.tdb): HCP_A3, type code %A, sha256 `04ec75b2710df32a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : LI NA : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001) Shengjun Zhang, Dongwon Shin, Zi-Kui Liu, Thermodynamic modeling of the Ca–Li–Na system, Calphad 27, 235-241 (2003).  
_assessment that models this phase_

## LIQUID (Li–Na)

- Id: `phase:li-na:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 360–2500 K, x(Na) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-na:liquid)

Names (5): _corpus: _corpus:phase:li-na:liquid  
_paper: _paper:10.1016/j.calphad.2003.09.001:Liquid, paper:10.1016/j.calphad.2003.09.001:Liquid2, paper:10.1016/j.calphad.2003.09.001:liquid2  
_tdb: _tdb:LiNa-03Zha-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LiNa-03Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/LiNa-03Zha-LB.tdb): LIQUID, type code %, sha256 `04ec75b2710df32a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : LI NA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2003.09.001](https://doi.org/10.1016/j.calphad.2003.09.001) Shengjun Zhang, Dongwon Shin, Zi-Kui Liu, Thermodynamic modeling of the Ca–Li–Na system, Calphad 27, 235-241 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1039/dt9750001490](https://doi.org/10.1039/dt9750001490) Michael G. Down, Peter Hubberstey, Richard J. Pulham, Sodium–lithium phase diagram: redetermination of the liquid immiscibility system by resistance measurement, J. Chem. Soc., Dalton Trans., 1490 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/0375-9601(75)90674-x](https://doi.org/10.1016/0375-9601%2875%2990674-x) E.S. Wu, H. Brumberger, Critical small-angle X-ray scattering of the liquid sodium-lithium system, Physics Letters A 53, 475-477 (1975).  
_cited as the source of values for this phase_
- [doi:10.1021/j150535a004](https://doi.org/10.1021/j150535a004) O. N. Salmon, D. H. Ahmann, The Lithiuim–Sodium Liquid Metal System, J. Phys. Chem. 60, 13-14 (1956).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevlett.27.1790](https://doi.org/10.1103/physrevlett.27.1790) H. K. Schürmann, R. D. Parks, Paraconductivity in Binary Metallic Liquids above the Critical Point, Phys. Rev. Lett. 27, 1790-1793 (1971).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
