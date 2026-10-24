# Bi–Na phases

> Bi–Na system: 7 phases (tier A 6, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-NA.html · Markdown: https://data.orchid-project.org/phases/pages/BI-NA.md

7 phases (tier A 6, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-NA) · [full JSON](https://data.orchid-project.org/phases/systems/BI-NA.json) · [Bi–Na system page](https://data.orchid-project.org/systems/BI-NA.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-NA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Na system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-na-a7-rhombohedral); _phase:bi-na:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Na) 0–0 | 4 | 1 |
| [BCC_A2](#phase-bi-na-bcc-a2); _phase:bi-na:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–370.87 K, x(Na) 1–1 | 0 | 1 |
| [BINA_L10](#phase-bi-na-bina-l10); _phase:bi-na:bina-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–717.64 K, x(Na) 0.5–0.5 | 9 | 1 |
| [BINA3_D018](#phase-bi-na-bina3-d018); _phase:bi-na:bina3-d018_ | Na3As · D0_18 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1125.92 K, x(Na) 0.75–0.75 | 15 | 1 |
| [FCC_A1](#phase-bi-na-fcc-a1); _phase:bi-na:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-na-hcp-a3); _phase:bi-na:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-bi-na-liquid); _phase:bi-na:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 370.87–2500 K, x(Na) 0–1 | 21 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Na)

- Id: `phase:bi-na:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Na) 0–0
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-na:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-na:a7-rhombohedral, corpus:phase:bi-na:rhombohedral-a7  
_paper: _paper:10.1016/j.tca.2013.01.029:Bi  
_tdb: _tdb:BiNa-13Liu.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiNa-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNa-13Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8c20e65805717473…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(70)90008-1](https://doi.org/10.1016/0022-5088%2870%2990008-1) C.E. Johnson, A.K. Fischer, New measurements for the sodium-bismuth phase diagram, Journal of the Less Common Metals 20, 339-344 (1970).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Na)

- Id: `phase:bi-na:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–370.87 K, x(Na) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-na:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-na:bcc-a2  
_tdb: _tdb:BiNa-13Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiNa-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNa-13Liu.tdb): BCC_A2, type code %B, sha256 `8c20e65805717473…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : BI NA% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase_

## BINA_L10 (Bi–Na)

- Id: `phase:bi-na:bina-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabhxs and oqmd-28744, space group 123
- Stoichiometry: Bi 0.5000, Na 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–717.64 K, x(Na) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-na:bina-l10)

Names (5): _corpus: _corpus:phase:bi-na:bina-l10  
_mp: _mp:mp-aaaabhxs  
_oqmd: _oqmd:oqmd-28744  
_paper: _paper:10.1016/j.tca.2013.01.029:BiNa  
_tdb: _tdb:BiNa-13Liu.tdb:BINA_L10  


### TDB models of BINA_L10 (1): PHASE and CONSTITUENT statements as written

[BiNa-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNa-13Liu.tdb): BINA_L10, type code %, sha256 `8c20e65805717473…`

~~~~text
50: PHASE BINA_L10 % 2 1 1 !
51: CONST BINA_L10 : BI : NA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(70)90008-1](https://doi.org/10.1016/0022-5088%2870%2990008-1) C.E. Johnson, A.K. Fischer, New measurements for the sodium-bismuth phase diagram, Journal of the Less Common Metals 20, 339-344 (1970).  
_cited as the source of values for this phase_

## BINA3_D018 (Bi–Na)

- Id: `phase:bi-na:bina3-d018`; status `assigned`
- Structure: Na3As · D0_18 · hP8 · P6_3/mmc (194); type `st:d0-18-na3as-hp8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.2500, Na 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1125.92 K, x(Na) 0.75–0.75
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-na:bina3-d018)

Names (3): _corpus: _corpus:phase:bi-na:bina3-d018  
_paper: _paper:10.1016/j.tca.2013.01.029:BiNa3  
_tdb: _tdb:BiNa-13Liu.tdb:BINA3_D018  


### TDB models of BINA3_D018 (1): PHASE and CONSTITUENT statements as written

[BiNa-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNa-13Liu.tdb): BINA3_D018, type code %, sha256 `8c20e65805717473…`

~~~~text
55: PHASE BINA3_D018 % 2 1 3 !
56: CONST BINA3_D018 : BI : NA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(70)90008-1](https://doi.org/10.1016/0022-5088%2870%2990008-1) C.E. Johnson, A.K. Fischer, New measurements for the sodium-bismuth phase diagram, Journal of the Less Common Metals 20, 339-344 (1970).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19000230136](https://doi.org/10.1002/zaac.19000230136) N. S. Kurnakow, Über die gegenseitigen Verbindungen der Metalle, Z. Anorg. Chem. 23, 439-462 (1900).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Na)

- Id: `phase:bi-na:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-na:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-na:fcc-a1  
_tdb: _tdb:BiNa-13Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiNa-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNa-13Liu.tdb): FCC_A1, type code %A, sha256 `8c20e65805717473…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : BI NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase_

## HCP_A3 (Bi–Na)

- Id: `phase:bi-na:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-na:hcp-a3)

Names (2): _corpus: _corpus:phase:bi-na:hcp-a3  
_tdb: _tdb:BiNa-13Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiNa-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNa-13Liu.tdb): HCP_A3, type code %A, sha256 `8c20e65805717473…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : BI NA : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase_

## LIQUID (Bi–Na)

- Id: `phase:bi-na:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 370.87–2500 K, x(Na) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-na:liquid)

Names (4): _corpus: _corpus:phase:bi-na:liquid  
_paper: _paper:10.1016/j.tca.2013.01.029:liq, paper:10.1016/j.tca.2013.01.029:liquid  
_tdb: _tdb:BiNa-13Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiNa-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNa-13Liu.tdb): LIQUID, type code %, sha256 `8c20e65805717473…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : BI BINA3 NA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.tca.2013.01.029](https://doi.org/10.1016/j.tca.2013.01.029) Yajun Liu, Zhitao Kang, Jiang Wang, Thermodynamic basis and related phase equilibria for Bi–Li and Bi–Na binary systems, Thermochimica Acta 558, 53-60 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(70)90008-1](https://doi.org/10.1016/0022-5088%2870%2990008-1) C.E. Johnson, A.K. Fischer, New measurements for the sodium-bismuth phase diagram, Journal of the Less Common Metals 20, 339-344 (1970).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19000230136](https://doi.org/10.1002/zaac.19000230136) N. S. Kurnakow, Über die gegenseitigen Verbindungen der Metalle, Z. Anorg. Chem. 23, 439-462 (1900).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02645966](https://doi.org/10.1007/bf02645966) J. Sangster, A.D. Pelton, The Bi–Li (bismuth–lithium) system, J. Phase Equilib. 12 (1991) 447–450.  
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
