# Cs–In phases

> Cs–In system: 7 phases (tier A 4, tier B 1, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CS-IN.html · Markdown: https://data.orchid-project.org/phases/pages/CS-IN.md

7 phases (tier A 4, tier B 1, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CS-IN) · [full JSON](https://data.orchid-project.org/phases/systems/CS-IN.json) · [Cs–In system page](https://data.orchid-project.org/systems/CS-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CS-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cs–In system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-cs-in-a6-tetragonal); _phase:cs-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.37 K, x(In) 1–1 | 0 | 1 |
| [BCC_A2](#phase-cs-in-bcc-a2); _phase:cs-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–301.59 K, x(In) 0–1e-05 | 0 | 1 |
| [CS2IN3](#phase-cs-in-cs2in3); _phase:cs-in:cs2in3_ | Cs2In3 · tI20 · I-4m2 (119) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–837.17 K, x(In) 0.6–0.6 | 4 | 1 |
| [CSIN3](#phase-cs-in-csin3); _phase:cs-in:csin3_ | Ga3Rb · tI24 · I-4m2 (119) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–757.07 K, x(In) 0.75–0.75 | 4 | 1 |
| [FCC_A1](#phase-cs-in-fcc-a1); _phase:cs-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-cs-in-hcp-a3); _phase:cs-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cs-in-liquid); _phase:cs-in:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 301.59–2500 K, x(In) 0–1 | 0 | 1 |

## TETRAGONAL_A6 (Cs–In)

- Id: `phase:cs-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.37 K, x(In) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-in:a6-tetragonal)

Names (2): _corpus: _corpus:phase:cs-in:a6-tetragonal  
_tdb: _tdb:CsIn-10Lee.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[CsIn-10Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CsIn-10Lee.tdb): TETRAGONAL_A6, type code %, sha256 `b36e9eae5cebe1d2…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.01.005](https://doi.org/10.1016/j.calphad.2010.01.005) Sung Hoon Lee, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of Cs–In system, Calphad 34, 134-137 (2010).  
_assessment that models this phase_

## BCC_A2 (Cs–In)

- Id: `phase:cs-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–301.59 K, x(In) 0–1e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-in:bcc-a2)

Names (2): _corpus: _corpus:phase:cs-in:bcc-a2  
_tdb: _tdb:CsIn-10Lee.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CsIn-10Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CsIn-10Lee.tdb): BCC_A2, type code %B, sha256 `b36e9eae5cebe1d2…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CS IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.01.005](https://doi.org/10.1016/j.calphad.2010.01.005) Sung Hoon Lee, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of Cs–In system, Calphad 34, 134-137 (2010).  
_assessment that models this phase_

## CS2IN3 (Cs–In)

- Id: `phase:cs-in:cs2in3`; status `assigned`
- Structure: Cs2In3 · tI20 · I-4m2 (119); type `st:cs2in3-ti20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cs 0.4000, In 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–837.17 K, x(In) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-in:cs2in3)

Names (3): _corpus: _corpus:phase:cs-in:cs2in3  
_paper: _paper:10.1016/j.calphad.2010.01.005:Cs2In3  
_tdb: _tdb:CsIn-10Lee.tdb:CS2IN3  


### TDB models of CS2IN3 (1): PHASE and CONSTITUENT statements as written

[CsIn-10Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CsIn-10Lee.tdb): CS2IN3, type code %, sha256 `b36e9eae5cebe1d2…`

~~~~text
45: PHASE CS2IN3 % 2 2 3 !
46: CONST CS2IN3 : CS : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2010.01.005](https://doi.org/10.1016/j.calphad.2010.01.005) Sung Hoon Lee, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of Cs–In system, Calphad 34, 134-137 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(85)90228-0](https://doi.org/10.1016/0022-5088%2885%2990228-0) S.P. Yatsenko, K.A. Tschuntonow, A.N. Orlow, Ya.P. Yarmolyuk, Yu.N. Hryn, Kristallstruktur von Cs2In3, Journal of the Less Common Metals 108, 339-343 (1985).  
_cited as the source of values for this phase_

## CSIN3 (Cs–In)

- Id: `phase:cs-in:csin3`; status `assigned`
- Structure: Ga3Rb · tI24 · I-4m2 (119); type `st:ga3rb-ti24`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Cs 0.2500, In 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–757.07 K, x(In) 0.75–0.75
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-in:csin3)

Names (5): _corpus: _corpus:phase:cs-in:csin3  
_mp: _mp:mp-aaabewhf  
_oqmd: _oqmd:oqmd-17138  
_paper: _paper:10.1016/j.calphad.2010.01.005:CsIn3  
_tdb: _tdb:CsIn-10Lee.tdb:CSIN3  


### TDB models of CSIN3 (1): PHASE and CONSTITUENT statements as written

[CsIn-10Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CsIn-10Lee.tdb): CSIN3, type code %, sha256 `b36e9eae5cebe1d2…`

~~~~text
50: PHASE CSIN3 % 2 1 3 !
51: CONST CSIN3 : CS : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2010.01.005](https://doi.org/10.1016/j.calphad.2010.01.005) Sung Hoon Lee, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of Cs–In system, Calphad 34, 134-137 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(84)90331-x](https://doi.org/10.1016/0022-5088%2884%2990331-x) K.A. Tschuntonow, S.P. Yatsenko, Yu.N. Hryn, Ya.P. Yarmolyuk, A.N. Orlow, Die Kristallstruktur von CsIn3, Journal of the Less Common Metals 99, 15-21 (1984).  
_cited as the source of values for this phase_

## FCC_A1 (Cs–In)

- Id: `phase:cs-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-in:fcc-a1)

Names (2): _corpus: _corpus:phase:cs-in:fcc-a1  
_tdb: _tdb:CsIn-10Lee.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CsIn-10Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CsIn-10Lee.tdb): FCC_A1, type code %A, sha256 `b36e9eae5cebe1d2…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CS IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.01.005](https://doi.org/10.1016/j.calphad.2010.01.005) Sung Hoon Lee, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of Cs–In system, Calphad 34, 134-137 (2010).  
_assessment that models this phase_

## HCP_A3 (Cs–In)

- Id: `phase:cs-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-in:hcp-a3)

Names (2): _corpus: _corpus:phase:cs-in:hcp-a3  
_tdb: _tdb:CsIn-10Lee.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CsIn-10Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CsIn-10Lee.tdb): HCP_A3, type code %, sha256 `b36e9eae5cebe1d2…`

~~~~text
35: PHASE HCP_A3 % 2 1 0.5 !
36: CONST HCP_A3 : CS IN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.01.005](https://doi.org/10.1016/j.calphad.2010.01.005) Sung Hoon Lee, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of Cs–In system, Calphad 34, 134-137 (2010).  
_assessment that models this phase_

## LIQUID (Cs–In)

- Id: `phase:cs-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 301.59–2500 K, x(In) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cs-in:liquid)

Names (2): _corpus: _corpus:phase:cs-in:liquid  
_tdb: _tdb:CsIn-10Lee.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CsIn-10Lee.tdb](https://orchid-project.org/data/databases/sgte-binary/CsIn-10Lee.tdb): LIQUID, type code %, sha256 `b36e9eae5cebe1d2…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CS IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.01.005](https://doi.org/10.1016/j.calphad.2010.01.005) Sung Hoon Lee, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of Cs–In system, Calphad 34, 134-137 (2010).  
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
