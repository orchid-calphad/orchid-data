# Co–H phases

> Co–H system: 5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-H.html · Markdown: https://data.orchid-project.org/phases/pages/CO-H.md

5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-H) · [full JSON](https://data.orchid-project.org/phases/systems/CO-H.json) · [Co–H system page](https://data.orchid-project.org/systems/CO-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–H system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-h-bcc-a2); _phase:co-h:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-co-h-fcc-a1); _phase:co-h:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 695.14–1768.48 K, x(H) 0–0.00035 | 0 | 1 |
| [GAS](#phase-co-h-gas); _phase:co-h:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 1–1 | 0 | 1 |
| [HCP_A3](#phase-co-h-hcp-a3); _phase:co-h:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–695.14 K, x(H) 0–6e-05 | 0 | 1 |
| [LIQUID](#phase-co-h-liquid); _phase:co-h:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1767.48–2500 K, x(H) 0–0.00073 | 0 | 1 |

## BCC_A2 (Co–H)

- Id: `phase:co-h:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-h:bcc-a2)

Names (2): _corpus: _corpus:phase:co-h:bcc-a2  
_tdb: _tdb:CoH-12Kim.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CoH-12Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoH-12Kim.tdb): BCC_A2, type code %B, sha256 `25f2231073fd723c…`

~~~~text
36: PHASE BCC_A2 %B 2 1 6 !
37: CONST BCC_A2 : CO : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2012.01.117](https://doi.org/10.1016/j.ijhydene.2012.01.117) Ki-Hyun Kim, Jae-Hyeok Shim, Byeong-Joo Lee, Effect of alloying elements (Al, Co, Fe, Ni) on the solubility of hydrogen in vanadium: A thermodynamic calculation, International Journal of Hydrogen Energy 37, 7836-7847 (2012).  
_assessment that models this phase_

## FCC_A1 (Co–H)

- Id: `phase:co-h:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 695.14–1768.48 K, x(H) 0–0.00035
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-h:fcc-a1)

Names (2): _corpus: _corpus:phase:co-h:fcc-a1  
_tdb: _tdb:CoH-12Kim.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CoH-12Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoH-12Kim.tdb): FCC_A1, type code %A, sha256 `25f2231073fd723c…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CO : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2012.01.117](https://doi.org/10.1016/j.ijhydene.2012.01.117) Ki-Hyun Kim, Jae-Hyeok Shim, Byeong-Joo Lee, Effect of alloying elements (Al, Co, Fe, Ni) on the solubility of hydrogen in vanadium: A thermodynamic calculation, International Journal of Hydrogen Energy 37, 7836-7847 (2012).  
_assessment that models this phase_

## GAS (Co–H)

- Id: `phase:co-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-h:gas)

Names (2): _corpus: _corpus:phase:co-h:gas  
_tdb: _tdb:CoH-12Kim.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CoH-12Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoH-12Kim.tdb): GAS, type code %, sha256 `25f2231073fd723c…`

~~~~text
44: PHASE GAS:G % 1 1 !
45: CONST GAS:G : H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2012.01.117](https://doi.org/10.1016/j.ijhydene.2012.01.117) Ki-Hyun Kim, Jae-Hyeok Shim, Byeong-Joo Lee, Effect of alloying elements (Al, Co, Fe, Ni) on the solubility of hydrogen in vanadium: A thermodynamic calculation, International Journal of Hydrogen Energy 37, 7836-7847 (2012).  
_assessment that models this phase_

## HCP_A3 (Co–H)

- Id: `phase:co-h:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–695.14 K, x(H) 0–6e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-h:hcp-a3)

Names (2): _corpus: _corpus:phase:co-h:hcp-a3  
_tdb: _tdb:CoH-12Kim.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CoH-12Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoH-12Kim.tdb): HCP_A3, type code %A, sha256 `25f2231073fd723c…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CO : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2012.01.117](https://doi.org/10.1016/j.ijhydene.2012.01.117) Ki-Hyun Kim, Jae-Hyeok Shim, Byeong-Joo Lee, Effect of alloying elements (Al, Co, Fe, Ni) on the solubility of hydrogen in vanadium: A thermodynamic calculation, International Journal of Hydrogen Energy 37, 7836-7847 (2012).  
_assessment that models this phase_

## LIQUID (Co–H)

- Id: `phase:co-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1767.48–2500 K, x(H) 0–0.00073
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-h:liquid)

Names (2): _corpus: _corpus:phase:co-h:liquid  
_tdb: _tdb:CoH-12Kim.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CoH-12Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoH-12Kim.tdb): LIQUID, type code %, sha256 `25f2231073fd723c…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CO H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2012.01.117](https://doi.org/10.1016/j.ijhydene.2012.01.117) Ki-Hyun Kim, Jae-Hyeok Shim, Byeong-Joo Lee, Effect of alloying elements (Al, Co, Fe, Ni) on the solubility of hydrogen in vanadium: A thermodynamic calculation, International Journal of Hydrogen Energy 37, 7836-7847 (2012).  
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
