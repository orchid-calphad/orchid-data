# C–Zr phases

> C–Zr system: 6 phases (tier A 4, liquid 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/C-ZR.md

6 phases (tier A 4, liquid 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/C-ZR.json) · [C–Zr system page](https://data.orchid-project.org/systems/C-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Zr system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-zr-a4-diamond); _phase:c-zr:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GRAPHITE_A9](#phase-c-zr-a9-graphite); _phase:c-zr:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1 | 0 | 1 |
| [BCC_A2](#phase-c-zr-bcc-a2); _phase:c-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1139.58–2130 K, x(C) 0–0.00528 | 9 | 1 |
| [FCC_A1](#phase-c-zr-fcc-a1); _phase:c-zr:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 1 of 1 calculated diagram(s): 300–3693.27 K, x(C) 0.35911–0.5 | 0 | 1 |
| [HCP_A3](#phase-c-zr-hcp-a3); _phase:c-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1159 K, x(C) 0–0.00735 | 0 | 1 |
| [LIQUID](#phase-c-zr-liquid); _phase:c-zr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2127.01–4000 K, x(C) 0–0.78212 | 16 | 1 |

## DIAMOND_A4 (C–Zr)

- Id: `phase:c-zr:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-zr:a4-diamond)

Names (3): _corpus: _corpus:phase:c-zr:a4-diamond, corpus:phase:c-zr:diamond-a4  
_tdb: _tdb:ZrC-95Fer-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[ZrC-95Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrC-95Fer-LB.tdb): DIAMOND_A4, type code %, sha256 `bc1756dee94f6955…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(94)01310-E](https://doi.org/10.1016/0925-8388%2894%2901310-E) A. Fernandez Guillermet, J. Alloys Compd., 217, 69-89(1995).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Zr)

- Id: `phase:c-zr:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-zr:a9-graphite)

Names (2): _corpus: _corpus:phase:c-zr:a9-graphite  
_tdb: _tdb:ZrC-95Fer-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (1): PHASE and CONSTITUENT statements as written

[ZrC-95Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrC-95Fer-LB.tdb): GRAPHITE_A9, type code %, sha256 `bc1756dee94f6955…`

~~~~text
45: PHASE GRAPHITE_A9 % 1 1 !
46: CONST GRAPHITE_A9 : C : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(94)01310-E](https://doi.org/10.1016/0925-8388%2894%2901310-E) A. Fernandez Guillermet, J. Alloys Compd., 217, 69-89(1995).  
_assessment that models this phase_

## BCC_A2 (C–Zr)

- Id: `phase:c-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1139.58–2130 K, x(C) 0–0.00528
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-zr:bcc-a2)

Names (4): _corpus: _corpus:phase:c-zr:bcc-a2  
_paper: _paper:10.1016/0925-8388(94)01310-e:β, paper:10.1361/105497102770331703:(βZr)  
_tdb: _tdb:ZrC-95Fer-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ZrC-95Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrC-95Fer-LB.tdb): BCC_A2, type code %B, sha256 `bc1756dee94f6955…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : ZR% : C VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(94)01310-E](https://doi.org/10.1016/0925-8388%2894%2901310-E) A. Fernandez Guillermet, J. Alloys Compd., 217, 69-89(1995).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1361/105497102770331703](https://doi.org/10.1361/105497102770331703) H. Bittermann, P. Rogl, Critical assessment and thermodynamic calculation of the ternary system C-Hf-Zr (Carbon-Zirconium-Hafnium), JPE 23, 218-235 (2002).  
_reports values for this phase_

## FCC_A1 (C–Zr)

- Id: `phase:c-zr:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3693.27 K, x(C) 0.35911–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-zr:fcc-a1)

Names (2): _corpus: _corpus:phase:c-zr:fcc-a1  
_tdb: _tdb:ZrC-95Fer-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ZrC-95Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrC-95Fer-LB.tdb): FCC_A1, type code %A, sha256 `bc1756dee94f6955…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : ZR : C% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(94)01310-E](https://doi.org/10.1016/0925-8388%2894%2901310-E) A. Fernandez Guillermet, J. Alloys Compd., 217, 69-89(1995).  
_assessment that models this phase_

## HCP_A3 (C–Zr)

- Id: `phase:c-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1159 K, x(C) 0–0.00735
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-zr:hcp-a3)

Names (2): _corpus: _corpus:phase:c-zr:hcp-a3  
_tdb: _tdb:ZrC-95Fer-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ZrC-95Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrC-95Fer-LB.tdb): HCP_A3, type code %A, sha256 `bc1756dee94f6955…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : ZR% : C VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(94)01310-E](https://doi.org/10.1016/0925-8388%2894%2901310-E) A. Fernandez Guillermet, J. Alloys Compd., 217, 69-89(1995).  
_assessment that models this phase_

## LIQUID (C–Zr)

- Id: `phase:c-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2127.01–4000 K, x(C) 0–0.78212
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-zr:liquid)

Names (3): _corpus: _corpus:phase:c-zr:liquid  
_paper: _paper:10.1016/0925-8388(94)01310-e:L  
_tdb: _tdb:ZrC-95Fer-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ZrC-95Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrC-95Fer-LB.tdb): LIQUID, type code %, sha256 `bc1756dee94f6955…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : C ZR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(94)01310-E](https://doi.org/10.1016/0925-8388%2894%2901310-E) A. Fernandez Guillermet, J. Alloys Compd., 217, 69-89(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19311980122](https://doi.org/10.1002/zaac.19311980122) C. Agte, K. Moers, Methoden zur Reindarstellung hochschmelzender Carbide, Nitride und Boride und Beschreibung einiger ihrer Eigenschaften, Z. Anorg. Allg. Chem. 198, 233-275 (1931).  
_cited as the source of values for this phase_
- [doi:10.1021/j100798a019](https://doi.org/10.1021/j100798a019) T. C. Wallace, C. P. Gutierrez, P. L. Stone, THE MOLYBDENUM—ZIRCONIUM—CARBON SYSTEM\<sup>1\</sup>, J. Phys. Chem. 67, 796-801 (1963).  
_cited as the source of values for this phase_

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
