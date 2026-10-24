# Ag–Al phases

> Ag–Al system: 5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-AL.html · Markdown: https://data.orchid-project.org/phases/pages/AG-AL.md

5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-AL) · [full JSON](https://data.orchid-project.org/phases/systems/AG-AL.json) · [Ag–Al system page](https://data.orchid-project.org/systems/AG-AL.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-AL.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Al system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ag-al-bcc-a2); _phase:ag-al:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 859.31–2500 K, x(Al) 0.20553–1 | 0 | 5 |
| [CUB_A13](#phase-ag-al-cub-a13); _phase:ag-al:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–740.16 K, x(Al) 0.16245–0.31021 | 0 | 5 |
| [FCC_A1](#phase-ag-al-fcc-a1); _phase:ag-al:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2499.72 K, x(Al) 0–1 | 25 | 5 |
| [HCP_A3](#phase-ag-al-hcp-a3); _phase:ag-al:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–1007.61 K, x(Al) 0.06933–0.99 | 0 | 5 |
| [LIQUID](#phase-ag-al-liquid); _phase:ag-al:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 829.98–2500 K, x(Al) 0–1 | 74 | 5 |

## BCC_A2 (Ag–Al)

- Id: `phase:ag-al:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 859.31–2500 K, x(Al) 0.20553–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-al:bcc-a2)

Names (6): _corpus: _corpus:phase:ag-al:bcc-a2  
_tdb: _tdb:AgAl-04Wit.tdb:BCC_A2, tdb:AgAl-20Ter.tdb:BCC_A2, tdb:AgAl-80Spe.tdb:BCC_A2, tdb:AgAl-87Spe.tdb:BCC_A2, tdb:AgAl-95Lim-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[AgAl-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-04Wit.tdb): BCC_A2, type code %B, sha256 `5e45c3ca7a36f2e6…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG AL : VA : !
~~~~

[AgAl-20Ter.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-20Ter.tdb): BCC_A2, type code %B, sha256 `a837f56ad4c96476…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : AG AL : VA : !
~~~~

[AgAl-80Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-80Spe.tdb): BCC_A2, type code %B, sha256 `f7ece3c580423ee3…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AG AL : VA : !
~~~~

[AgAl-87Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-87Spe.tdb): BCC_A2, type code %B, sha256 `bc64253f66e7370a…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : AG AL : VA : !
~~~~

[AgAl-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-95Lim-LB.tdb): BCC_A2, type code %B, sha256 `50d3ba34c63e1b8b…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AG AL : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF00810049](https://doi.org/10.1007/BF00810049) P.J. Spencer, O. Kubaschewski, Monatshefte Chem., 118, 155-67(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.S. Lim, P.L. Rossiter, J.E. Tibballs, Calphad, 19, 131-41(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101739](https://doi.org/10.1016/j.calphad.2020.101739) S. Terlicka, A. Debski, W. Gierlotka, A. Wierzbicka-Miernik, A. Budziak, A. Sypien, M. Zabrocki, W. Gasior, Calphad, 68, 101739(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase_

## CUB_A13 (Ag–Al)

- Id: `phase:ag-al:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–740.16 K, x(Al) 0.16245–0.31021
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-al:cub-a13)

Names (6): _corpus: _corpus:phase:ag-al:cub-a13  
_tdb: _tdb:AgAl-04Wit.tdb:CUB_A13, tdb:AgAl-20Ter.tdb:CUB_A13, tdb:AgAl-80Spe.tdb:CUB_A13, tdb:AgAl-87Spe.tdb:CUB_A13, tdb:AgAl-95Lim-LB.tdb:CUB_A13  


### TDB models of CUB_A13 (5): PHASE and CONSTITUENT statements as written

[AgAl-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-04Wit.tdb): CUB_A13, type code %, sha256 `5e45c3ca7a36f2e6…`

~~~~text
43: PHASE CUB_A13 % 2 1 1 !
44: CONST CUB_A13 : AG AL : VA : !
~~~~

[AgAl-20Ter.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-20Ter.tdb): CUB_A13, type code %, sha256 `a837f56ad4c96476…`

~~~~text
52: PHASE CUB_A13 % 2 1 1 !
53: CONST CUB_A13 : AG AL : VA : !
~~~~

[AgAl-80Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-80Spe.tdb): CUB_A13, type code %, sha256 `f7ece3c580423ee3…`

~~~~text
46: PHASE CUB_A13 % 2 1 1 !
47: CONST CUB_A13 : AG AL : VA : !
~~~~

[AgAl-87Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-87Spe.tdb): CUB_A13, type code %, sha256 `bc64253f66e7370a…`

~~~~text
51: PHASE CUB_A13 % 2 1 1 !
52: CONST CUB_A13 : AG AL : VA : !
~~~~

[AgAl-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-95Lim-LB.tdb): CUB_A13, type code %, sha256 `50d3ba34c63e1b8b…`

~~~~text
42: PHASE CUB_A13 % 2 1 1 !
43: CONST CUB_A13 : AG AL : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF00810049](https://doi.org/10.1007/BF00810049) P.J. Spencer, O. Kubaschewski, Monatshefte Chem., 118, 155-67(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.S. Lim, P.L. Rossiter, J.E. Tibballs, Calphad, 19, 131-41(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101739](https://doi.org/10.1016/j.calphad.2020.101739) S. Terlicka, A. Debski, W. Gierlotka, A. Wierzbicka-Miernik, A. Budziak, A. Sypien, M. Zabrocki, W. Gasior, Calphad, 68, 101739(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase_

## FCC_A1 (Ag–Al)

- Id: `phase:ag-al:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2499.72 K, x(Al) 0–1
- Literature: 25 values (25 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-al:fcc-a1)

Names (10): _corpus: _corpus:phase:ag-al:fcc-a1  
_paper: _paper:10.1007/bf00810049:(Ag), paper:10.1007/bf00810049:(Al), paper:10.1016/j.jallcom.2004.04.126:(Ag), paper:10.1016/j.jallcom.2004.04.126:(Al)  
_tdb: _tdb:AgAl-04Wit.tdb:FCC_A1, tdb:AgAl-20Ter.tdb:FCC_A1, tdb:AgAl-80Spe.tdb:FCC_A1, tdb:AgAl-87Spe.tdb:FCC_A1, tdb:AgAl-95Lim-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[AgAl-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-04Wit.tdb): FCC_A1, type code %A, sha256 `5e45c3ca7a36f2e6…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% AL% : VA : !
~~~~

[AgAl-20Ter.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-20Ter.tdb): FCC_A1, type code %A, sha256 `a837f56ad4c96476…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : AG% AL% : VA : !
~~~~

[AgAl-80Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-80Spe.tdb): FCC_A1, type code %A, sha256 `f7ece3c580423ee3…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AG% AL% : VA : !
~~~~

[AgAl-87Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-87Spe.tdb): FCC_A1, type code %A, sha256 `bc64253f66e7370a…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : AG% AL% : VA : !
~~~~

[AgAl-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-95Lim-LB.tdb): FCC_A1, type code %A, sha256 `50d3ba34c63e1b8b…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AG% AL% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF00810049](https://doi.org/10.1007/BF00810049) P.J. Spencer, O. Kubaschewski, Monatshefte Chem., 118, 155-67(1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.S. Lim, P.L. Rossiter, J.E. Tibballs, Calphad, 19, 131-41(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101739](https://doi.org/10.1016/j.calphad.2020.101739) S. Terlicka, A. Debski, W. Gierlotka, A. Wierzbicka-Miernik, A. Budziak, A. Sypien, M. Zabrocki, W. Gasior, Calphad, 68, 101739(2020).  
_assessment that models this phase_

## HCP_A3 (Ag–Al)

- Id: `phase:ag-al:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–1007.61 K, x(Al) 0.06933–0.99
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-al:hcp-a3)

Names (6): _corpus: _corpus:phase:ag-al:hcp-a3  
_tdb: _tdb:AgAl-04Wit.tdb:HCP_A3, tdb:AgAl-20Ter.tdb:HCP_A3, tdb:AgAl-80Spe.tdb:HCP_A3, tdb:AgAl-87Spe.tdb:HCP_A3, tdb:AgAl-95Lim-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[AgAl-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-04Wit.tdb): HCP_A3, type code %A, sha256 `5e45c3ca7a36f2e6…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG AL : VA : !
~~~~

[AgAl-20Ter.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-20Ter.tdb): HCP_A3, type code %A, sha256 `a837f56ad4c96476…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : AG AL : VA : !
~~~~

[AgAl-80Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-80Spe.tdb): HCP_A3, type code %A, sha256 `f7ece3c580423ee3…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AG AL : VA : !
~~~~

[AgAl-87Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-87Spe.tdb): HCP_A3, type code %A, sha256 `bc64253f66e7370a…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : AG AL : VA : !
~~~~

[AgAl-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-95Lim-LB.tdb): HCP_A3, type code %A, sha256 `50d3ba34c63e1b8b…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AG AL : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF00810049](https://doi.org/10.1007/BF00810049) P.J. Spencer, O. Kubaschewski, Monatshefte Chem., 118, 155-67(1987).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.S. Lim, P.L. Rossiter, J.E. Tibballs, Calphad, 19, 131-41(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101739](https://doi.org/10.1016/j.calphad.2020.101739) S. Terlicka, A. Debski, W. Gierlotka, A. Wierzbicka-Miernik, A. Budziak, A. Sypien, M. Zabrocki, W. Gasior, Calphad, 68, 101739(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase_

## LIQUID (Ag–Al)

- Id: `phase:ag-al:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 829.98–2500 K, x(Al) 0–1
- Literature: 74 values (74 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-al:liquid)

Names (9): _corpus: _corpus:phase:ag-al:liquid  
_paper: _paper:10.1007/bf00810049:L, paper:10.1016/j.jallcom.2004.04.126:L, paper:10.1016/j.jallcom.2004.04.126:liquid  
_tdb: _tdb:AgAl-04Wit.tdb:LIQUID, tdb:AgAl-20Ter.tdb:LIQUID, tdb:AgAl-80Spe.tdb:LIQUID, tdb:AgAl-87Spe.tdb:LIQUID, tdb:AgAl-95Lim-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[AgAl-04Wit.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-04Wit.tdb): LIQUID, type code %, sha256 `5e45c3ca7a36f2e6…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG AL : !
~~~~

[AgAl-20Ter.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-20Ter.tdb): LIQUID, type code %, sha256 `a837f56ad4c96476…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : AG AL : !
~~~~

[AgAl-80Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-80Spe.tdb): LIQUID, type code %, sha256 `f7ece3c580423ee3…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AG AL : !
~~~~

[AgAl-87Spe.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-87Spe.tdb): LIQUID, type code %, sha256 `bc64253f66e7370a…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : AG AL : !
~~~~

[AgAl-95Lim-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgAl-95Lim-LB.tdb): LIQUID, type code %, sha256 `50d3ba34c63e1b8b…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AG AL : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2004.04.126](https://doi.org/10.1016/j.jallcom.2004.04.126) V.T. Witusiewicz, U. Hecht, S.G. Fries, S. Rex, The Ag–Al–Cu system, Journal of Alloys and Compounds 385, 133-143 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF00810049](https://doi.org/10.1007/BF00810049) P.J. Spencer, O. Kubaschewski, Monatshefte Chem., 118, 155-67(1987).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00014-6](https://doi.org/10.1016/0364-5916%2895%2900014-6) S.S. Lim, P.L. Rossiter, J.E. Tibballs, Calphad, 19, 131-41(1995).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101739](https://doi.org/10.1016/j.calphad.2020.101739) S. Terlicka, A. Debski, W. Gierlotka, A. Wierzbicka-Miernik, A. Budziak, A. Sypien, M. Zabrocki, W. Gasior, Calphad, 68, 101739(2020).  
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
