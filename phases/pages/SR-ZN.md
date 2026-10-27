# Sr–Zn phases

> Sr–Zn system: 9 phases (tier A 6, tier C 2, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SR-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/SR-ZN.md

9 phases (tier A 6, tier C 2, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SR-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/SR-ZN.json) · [Sr–Zn system page](https://data.orchid-project.org/systems/SR-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SR-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sr–Zn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-sr-zn-bcc-a2); _phase:sr-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 815.68–1050 K, x(Zn) 0–0.0059 | 1 | 1 |
| [FCC_A1](#phase-sr-zn-fcc-a1); _phase:sr-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–820 K, x(Zn) 0–0.00487 | 3 | 1 |
| [HCP_A3](#phase-sr-zn-hcp-a3); _phase:sr-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–692.68 K, x(Zn) 1–1 | 1 | 1 |
| [LIQUID](#phase-sr-zn-liquid); _phase:sr-zn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 642.5–2500 K, x(Zn) 0–1 | 27 | 1 |
| [SRZN_B27](#phase-sr-zn-srzn-b27); _phase:sr-zn:srzn-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–705.53 K, x(Zn) 0.5–0.5 | 4 | 1 |
| [SRZN13_D23](#phase-sr-zn-srzn13-d23); _phase:sr-zn:srzn13-d23_ | NaZn13 · D2_3 · cF112 · Fm-3c (226) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1103.08 K, x(Zn) 0.92857–0.92857 | 5 | 1 |
| [SRZN2](#phase-sr-zn-srzn2); _phase:sr-zn:srzn2_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–847.1 K, x(Zn) 0.66667–0.66667 | 6 | 1 |
| [SRZN5_ALPHA](#phase-sr-zn-srzn5-alpha); _phase:sr-zn:srzn5-alpha_ | SrZn5 · oP24 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–896.55 K, x(Zn) 0.83333–0.83333 | 4 | 1 |
| [SRZN5_D2D](#phase-sr-zn-srzn5-d2d); _phase:sr-zn:srzn5-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 896.55–923.04 K, x(Zn) 0.83333–0.83333 | 4 | 1 |

## BCC_A2 (Sr–Zn)

- Id: `phase:sr-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 815.68–1050 K, x(Zn) 0–0.0059
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:bcc-a2)

Names (3): _corpus: _corpus:phase:sr-zn:bcc-a2  
_paper: _paper:10.1361/105497103770330325:bcc  
_tdb: _tdb:SrZn-03Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): BCC_A2, type code %B, sha256 `76bc25ec714bc201…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SR ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Sr–Zn)

- Id: `phase:sr-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–820 K, x(Zn) 0–0.00487
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:fcc-a1)

Names (3): _corpus: _corpus:phase:sr-zn:fcc-a1  
_paper: _paper:10.1361/105497103770330325:fcc  
_tdb: _tdb:SrZn-03Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): FCC_A1, type code %A, sha256 `76bc25ec714bc201…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SR ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90226-6](https://doi.org/10.1016/0022-5088%2883%2990226-6) G. Bruzzone, F. Merlo, The Sr-Zn system, Journal of the Less Common Metals 92, 75-79 (1983).  
_cited as the source of values for this phase_

## HCP_A3 (Sr–Zn)

- Id: `phase:sr-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–692.68 K, x(Zn) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:hcp-a3)

Names (3): _corpus: _corpus:phase:sr-zn:hcp-a3  
_paper: _paper:10.1361/105497103770330325:hcp  
_tdb: _tdb:SrZn-03Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): HCP_A3, type code %A, sha256 `76bc25ec714bc201…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SR ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Sr–Zn)

- Id: `phase:sr-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 642.5–2500 K, x(Zn) 0–1
- Literature: 27 values (27 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:liquid)

Names (3): _corpus: _corpus:phase:sr-zn:liquid  
_paper: _paper:10.1361/105497103770330325:L  
_tdb: _tdb:SrZn-03Zho.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): LIQUID, type code %, sha256 `76bc25ec714bc201…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SR ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90226-6](https://doi.org/10.1016/0022-5088%2883%2990226-6) G. Bruzzone, F. Merlo, The Sr-Zn system, Journal of the Less Common Metals 92, 75-79 (1983).  
_cited as the source of values for this phase_

## SRZN_B27 (Sr–Zn)

- Id: `phase:sr-zn:srzn-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaasvk and oqmd-647530, space group 62
- Stoichiometry: Sr 0.5000, Zn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–705.53 K, x(Zn) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:srzn-b27)

Names (5): _corpus: _corpus:phase:sr-zn:srzn-b27  
_mp: _mp:mp-aaaaasvk  
_oqmd: _oqmd:oqmd-647530  
_paper: _paper:10.1361/105497103770330325:SrZn  
_tdb: _tdb:SrZn-03Zho.tdb:SRZN_B27  


### TDB models of SRZN_B27 (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): SRZN_B27, type code %, sha256 `76bc25ec714bc201…`

~~~~text
44: PHASE SRZN_B27 % 2 1 1 !
45: CONST SRZN_B27 : SR : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90226-6](https://doi.org/10.1016/0022-5088%2883%2990226-6) G. Bruzzone, F. Merlo, The Sr-Zn system, Journal of the Less Common Metals 92, 75-79 (1983).  
_cited as the source of values for this phase_

## SRZN13_D23 (Sr–Zn)

- Id: `phase:sr-zn:srzn13-d23`; status `assigned`
- Structure: NaZn13 · D2_3 · cF112 · Fm-3c (226); type `st:d2-3-nazn13-cf112`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabmhdj and oqmd-31093, space group 226
- Stoichiometry: Sr 0.0714, Zn 0.9286
- Stability: stable in 1 of 1 calculated diagram(s): 300–1103.08 K, x(Zn) 0.92857–0.92857
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:srzn13-d23)

Names (5): _corpus: _corpus:phase:sr-zn:srzn13-d23  
_mp: _mp:mp-aaabmhdj  
_oqmd: _oqmd:oqmd-31093  
_paper: _paper:10.1361/105497103770330325:SrZn13  
_tdb: _tdb:SrZn-03Zho.tdb:SRZN13_D23  


### TDB models of SRZN13_D23 (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): SRZN13_D23, type code %, sha256 `76bc25ec714bc201…`

~~~~text
64: PHASE SRZN13_D23 % 2 1 13 !
65: CONST SRZN13_D23 : SR : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90226-6](https://doi.org/10.1016/0022-5088%2883%2990226-6) G. Bruzzone, F. Merlo, The Sr-Zn system, Journal of the Less Common Metals 92, 75-79 (1983).  
_cited as the source of values for this phase_

## SRZN2 (Sr–Zn)

- Id: `phase:sr-zn:srzn2`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sr 0.3333, Zn 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–847.1 K, x(Zn) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:srzn2)

Names (3): _corpus: _corpus:phase:sr-zn:srzn2  
_paper: _paper:10.1361/105497103770330325:SrZn2  
_tdb: _tdb:SrZn-03Zho.tdb:SRZN2  


### TDB models of SRZN2 (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): SRZN2, type code %, sha256 `76bc25ec714bc201…`

~~~~text
49: PHASE SRZN2 % 2 1 2 !
50: CONST SRZN2 : SR : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90226-6](https://doi.org/10.1016/0022-5088%2883%2990226-6) G. Bruzzone, F. Merlo, The Sr-Zn system, Journal of the Less Common Metals 92, 75-79 (1983).  
_cited as the source of values for this phase_

## SRZN5_ALPHA (Sr–Zn)

- Id: `phase:sr-zn:srzn5-alpha`; status `assigned`
- Structure: SrZn5 · oP24 · Pnma (62); type `st:srzn5-op24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sr 0.1667, Zn 0.8333
- Stability: stable in 1 of 1 calculated diagram(s): 300–896.55 K, x(Zn) 0.83333–0.83333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:srzn5-alpha)

Names (3): _corpus: _corpus:phase:sr-zn:srzn5-alpha  
_paper: _paper:10.1361/105497103770330325:αSrZn5  
_tdb: _tdb:SrZn-03Zho.tdb:SRZN5_ALPHA  


### TDB models of SRZN5_ALPHA (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): SRZN5_ALPHA, type code %, sha256 `76bc25ec714bc201…`

~~~~text
54: PHASE SRZN5_ALPHA % 2 1 5 !
55: CONST SRZN5_ALPHA : SR : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90226-6](https://doi.org/10.1016/0022-5088%2883%2990226-6) G. Bruzzone, F. Merlo, The Sr-Zn system, Journal of the Less Common Metals 92, 75-79 (1983).  
_cited as the source of values for this phase_

## SRZN5_D2D (Sr–Zn)

- Id: `phase:sr-zn:srzn5-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Sr 0.1667, Zn 0.8333
- Stability: stable in 1 of 1 calculated diagram(s): 896.55–923.04 K, x(Zn) 0.83333–0.83333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sr-zn:srzn5-d2d)

Names (3): _corpus: _corpus:phase:sr-zn:srzn5-d2d  
_paper: _paper:10.1361/105497103770330325:βSrZn5  
_tdb: _tdb:SrZn-03Zho.tdb:SRZN5_D2D  


### TDB models of SRZN5_D2D (1): PHASE and CONSTITUENT statements as written

[SrZn-03Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/SrZn-03Zho.tdb): SRZN5_D2D, type code %, sha256 `76bc25ec714bc201…`

~~~~text
59: PHASE SRZN5_D2D % 2 1 5 !
60: CONST SRZN5_D2D : SR : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330325](https://doi.org/10.1361/105497103770330325) Yu Zhong, Koray Ozturk, Zi-Kui Liu, Thermodynamic modeling of the Ca-Sr-Zn ternary system, JPE 24, 340-346 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(83)90226-6](https://doi.org/10.1016/0022-5088%2883%2990226-6) G. Bruzzone, F. Merlo, The Sr-Zn system, Journal of the Less Common Metals 92, 75-79 (1983).  
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
