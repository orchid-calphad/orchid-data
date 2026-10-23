# Cu–H phases

> Cu–H system: 7 phases (tier A 5, liquid 1, gas 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-H.html · Markdown: https://data.orchid-project.org/phases/pages/CU-H.md

7 phases (tier A 5, liquid 1, gas 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-H) · [full JSON](https://data.orchid-project.org/phases/systems/CU-H.json) · [Cu–H system page](https://data.orchid-project.org/systems/CU-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–H system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-h-bcc-a2); _phase:cu-h:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [CUH_B3](#phase-cu-h-cuh-b3); _phase:cu-h:cuh-b3_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CUH_B4](#phase-cu-h-cuh-b4); _phase:cu-h:cuh-b4_ | ZnS (wurtzite) · B4 · hP4 · P6_3mc (186) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-cu-h-fcc-a1); _phase:cu-h:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1360.53 K, x(H) 0–0.0001 | 0 | 2 |
| [GAS](#phase-cu-h-gas); _phase:cu-h:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0.89356–1 | 0 | 2 |
| [HCP_A3](#phase-cu-h-hcp-a3); _phase:cu-h:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-cu-h-liquid); _phase:cu-h:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1357.53–2500 K, x(H) 0–0.00197 | 0 | 2 |

## BCC_A2 (Cu–H)

- Id: `phase:cu-h:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-h:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-h:bcc-a2  
_tdb: _tdb:CuH-07Hua.tdb:BCC_A2, tdb:CuH-14Mag.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CuH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-07Hua.tdb): BCC_A2, type code %B, sha256 `49646b7ec4a6535d…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CU : VA : !
~~~~

[CuH-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb): BCC_A2, type code %B, sha256 `631979327e19b67c…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_

## CUH_B3 (Cu–H)

- Id: `phase:cu-h:cuh-b3`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.5000, H 0.5000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-h:cuh-b3)

Names (2): _corpus: _corpus:phase:cu-h:cuh-b3  
_tdb: _tdb:CuH-14Mag.tdb:CUH_B3  


### TDB models of CUH_B3 (1): PHASE and CONSTITUENT statements as written

[CuH-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb): CUH_B3, type code %, sha256 `631979327e19b67c…`

~~~~text
50: PHASE CUH_B3 % 2 1 1 !
51: CONST CUH_B3 : CU : H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_

## CUH_B4 (Cu–H)

- Id: `phase:cu-h:cuh-b4`; status `assigned`
- Structure: ZnS (wurtzite) · B4 · hP4 · P6_3mc (186); type `st:b4-zns-wurtzite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 0.5000, H 0.5000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-h:cuh-b4)

Names (2): _corpus: _corpus:phase:cu-h:cuh-b4  
_tdb: _tdb:CuH-14Mag.tdb:CUH_B4  


### TDB models of CUH_B4 (1): PHASE and CONSTITUENT statements as written

[CuH-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb): CUH_B4, type code %, sha256 `631979327e19b67c…`

~~~~text
55: PHASE CUH_B4 % 2 1 1 !
56: CONST CUH_B4 : CU : H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_

## FCC_A1 (Cu–H)

- Id: `phase:cu-h:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1360.53 K, x(H) 0–0.0001
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-h:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-h:fcc-a1  
_tdb: _tdb:CuH-07Hua.tdb:FCC_A1, tdb:CuH-14Mag.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-07Hua.tdb): FCC_A1, type code %A, sha256 `49646b7ec4a6535d…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CU% : H VA% : !
~~~~

[CuH-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb): FCC_A1, type code %A, sha256 `631979327e19b67c…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CU% : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_

## GAS (Cu–H)

- Id: `phase:cu-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0.89356–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-h:gas)

Names (3): _corpus: _corpus:phase:cu-h:gas  
_tdb: _tdb:CuH-07Hua.tdb:GAS, tdb:CuH-14Mag.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[CuH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-07Hua.tdb): GAS, type code %, sha256 `49646b7ec4a6535d…`

~~~~text
44: PHASE GAS:G % 1 1 !
45: CONST GAS:G : CU CU2 CUH H H2 : !
~~~~

[CuH-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb): GAS, type code %, sha256 `631979327e19b67c…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : CU CU2 CUH H H2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_

## HCP_A3 (Cu–H)

- Id: `phase:cu-h:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-h:hcp-a3)

Names (3): _corpus: _corpus:phase:cu-h:hcp-a3  
_tdb: _tdb:CuH-07Hua.tdb:HCP_A3, tdb:CuH-14Mag.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CuH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-07Hua.tdb): HCP_A3, type code %A, sha256 `49646b7ec4a6535d…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CU : VA : !
~~~~

[CuH-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb): HCP_A3, type code %A, sha256 `631979327e19b67c…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_

## LIQUID (Cu–H)

- Id: `phase:cu-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1357.53–2500 K, x(H) 0–0.00197
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-h:liquid)

Names (3): _corpus: _corpus:phase:cu-h:liquid  
_tdb: _tdb:CuH-07Hua.tdb:LIQUID, tdb:CuH-14Mag.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CuH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-07Hua.tdb): LIQUID, type code %, sha256 `49646b7ec4a6535d…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CU H : !
~~~~

[CuH-14Mag.tdb](https://orchid-project.org/data/databases/sgte-binary/CuH-14Mag.tdb): LIQUID, type code %, sha256 `631979327e19b67c…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CU H : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.09.004](https://doi.org/10.1016/j.calphad.2014.09.004) Hans Magnusson, Karin Frisk, Thermodynamic evaluation of the copper-rich part of the CuHOSP system at low temperatures, Calphad 47, 148-160 (2014).  
_assessment that models this phase_

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
