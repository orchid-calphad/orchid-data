# F–Na phases

> F–Na system: 7 phases (tier A 4, liquid 2, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/F-NA.html · Markdown: https://data.orchid-project.org/phases/pages/F-NA.md

7 phases (tier A 4, liquid 2, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=F-NA) · [full JSON](https://data.orchid-project.org/phases/systems/F-NA.json) · [F–Na system page](https://data.orchid-project.org/systems/F-NA.html) · [Markdown](https://data.orchid-project.org/phases/pages/F-NA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the F–Na system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-f-na-bcc-a2); _phase:f-na:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–370.87 K, x(F) 0–0 | 1 | 1 |
| [FCC_A1](#phase-f-na-fcc-a1); _phase:f-na:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-f-na-gas); _phase:f-na:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(F) 0–1 | 2 | 1 |
| [HCP_A3](#phase-f-na-hcp-a3); _phase:f-na:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-f-na-ion); _phase:f-na:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 370.87–2057.75 K, x(F) 0–0.5 | 0 | 1 |
| [LIQUID](#phase-f-na-liquid); _phase:f-na:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 380–470 K | 6 | 1 |
| [NAF_B1](#phase-f-na-naf-b1); _phase:f-na:naf-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1269 K, x(F) 0.5–0.5 | 4 | 1 |

## BCC_A2 (F–Na)

- Id: `phase:f-na:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–370.87 K, x(F) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-na:bcc-a2)

Names (3): _corpus: _corpus:phase:f-na:bcc-a2  
_paper: _paper:10.1016/j.msea.2005.11.037:bcc  
_tdb: _tdb:NaF-06Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NaF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NaF-06Zha.tdb): BCC_A2, type code %B, sha256 `33d049d9c6fd6809…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (F–Na)

- Id: `phase:f-na:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-na:fcc-a1)

Names (2): _corpus: _corpus:phase:f-na:fcc-a1  
_tdb: _tdb:NaF-06Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NaF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NaF-06Zha.tdb): FCC_A1, type code %A, sha256 `33d049d9c6fd6809…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase_

## GAS (F–Na)

- Id: `phase:f-na:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(F) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-na:gas)

Names (3): _corpus: _corpus:phase:f-na:gas  
_paper: _paper:10.1016/j.msea.2005.11.037:Gas  
_tdb: _tdb:NaF-06Zha.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[NaF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NaF-06Zha.tdb): GAS, type code %, sha256 `33d049d9c6fd6809…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : F F2 NA NA2 NAF NA2F2 NA3F3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (F–Na)

- Id: `phase:f-na:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-na:hcp-a3)

Names (2): _corpus: _corpus:phase:f-na:hcp-a3  
_tdb: _tdb:NaF-06Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NaF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NaF-06Zha.tdb): HCP_A3, type code %A, sha256 `33d049d9c6fd6809…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase_

## ION (F–Na)

- Id: `phase:f-na:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 370.87–2057.75 K, x(F) 0–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-na:ion)

Names (2): _corpus: _corpus:phase:f-na:ion  
_tdb: _tdb:NaF-06Zha.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[NaF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NaF-06Zha.tdb): ION, type code %, sha256 `33d049d9c6fd6809…`

~~~~text
32: PHASE ION:Y % 2 1 1 !
33: CONST ION:Y : NA+1 : F-1 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase_

## LIQUID (F–Na)

- Id: `phase:f-na:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Na 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 380–470 K
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-na:liquid)

Names (5): _corpus: _corpus:phase:f-na:liquid  
_paper: _paper:10.1016/j.msea.2005.11.037:Liquid, paper:10.1016/j.msea.2005.11.037:liquid, paper:10.1016/j.msea.2005.11.037:liquid 2  
_tdb: _tdb:NaF-06Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NaF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NaF-06Zha.tdb): LIQUID, type code %, sha256 `33d049d9c6fd6809…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : NA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ja01607a016](https://doi.org/10.1021/ja01607a016) M. A. Bredig, J. W. Johnson, Wm. T. Smith, Miscibility of Liquid Metals with Salts. I. The Sodium-Sodium Halide Systems\<sup>1\</sup>, J. Am. Chem. Soc. 77, 307-312 (1955).  
_cited as the source of values for this phase_

## NAF_B1 (F–Na)

- Id: `phase:f-na:naf-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabag and oqmd-5686, space group 225
- Stoichiometry: F 0.5000, Na 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1269 K, x(F) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:f-na:naf-b1)

Names (5): _corpus: _corpus:phase:f-na:naf-b1  
_mp: _mp:mp-aaaaabag  
_oqmd: _oqmd:oqmd-5686  
_paper: _paper:10.1016/j.msea.2005.11.037:NaF  
_tdb: _tdb:NaF-06Zha.tdb:NAF_B1  


### TDB models of NAF_B1 (1): PHASE and CONSTITUENT statements as written

[NaF-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NaF-06Zha.tdb): NAF_B1, type code %, sha256 `33d049d9c6fd6809…`

~~~~text
55: PHASE NAF_B1 % 2 1 1 !
56: CONST NAF_B1 : NA : F : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ja01607a016](https://doi.org/10.1021/ja01607a016) M. A. Bredig, J. W. Johnson, Wm. T. Smith, Miscibility of Liquid Metals with Salts. I. The Sodium-Sodium Halide Systems\<sup>1\</sup>, J. Am. Chem. Soc. 77, 307-312 (1955).  
_cited as the source of values for this phase_

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
