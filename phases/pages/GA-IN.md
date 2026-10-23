# Ga–In phases

> Ga–In system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-IN.html · Markdown: https://data.orchid-project.org/phases/pages/GA-IN.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-IN) · [full JSON](https://data.orchid-project.org/phases/systems/GA-IN.json) · [Ga–In system page](https://data.orchid-project.org/systems/GA-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–In system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-in-a11-orthorhombic); _phase:ga-in:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 299.05–302.91 K, x(In) 0–0 | 6 | 3 |
| [TETRAGONAL_A6](#phase-ga-in-a6-tetragonal); _phase:ga-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 297.85–429.75 K, x(In) 0.96007–1 | 2 | 3 |
| [BCC_A2](#phase-ga-in-bcc-a2); _phase:ga-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-ga-in-fcc-a1); _phase:ga-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-ga-in-hcp-a3); _phase:ga-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-ga-in-liquid); _phase:ga-in:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 297.85–2500 K, x(In) 0–1 | 0 | 3 |

## ORTHORHOMBIC_A11 (Ga–In)

- Id: `phase:ga-in:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 299.05–302.91 K, x(In) 0–0
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-in:a11-orthorhombic)

Names (6): _corpus: _corpus:phase:ga-in:a11-orthorhombic  
_paper: _paper:10.1007/bf02663677:αGa, paper:10.1007/bf02663677:γGa  
_tdb: _tdb:GaIn-78Ans.tdb:ORTHORHOMBIC_A11, tdb:GaIn-90Rug-LB.tdb:ORTHORHOMBIC_A11, tdb:GaIn-91And.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (3): PHASE and CONSTITUENT statements as written

[GaIn-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-78Ans.tdb): ORTHORHOMBIC_A11, type code %, sha256 `a710b6be14e94849…`

~~~~text
49: PHASE ORTHORHOMBIC_A11 % 1 1 !
50: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaIn-90Rug-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-90Rug-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `8873223ef7171edc…`

~~~~text
45: PHASE ORTHORHOMBIC_A11 % 1 1 !
46: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaIn-91And.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-91And.tdb): ORTHORHOMBIC_A11, type code %, sha256 `4015efc6acf86024…`

~~~~text
50: PHASE ORTHORHOMBIC_A11 % 1 1 !
51: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02663677](https://doi.org/10.1007/BF02663677) T.J. Anderson, I. Ansara, J. Phase Equilib., 12, 64-72(1991).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90013-P](https://doi.org/10.1016/0364-5916%2890%2990013-P) B.C. Rugg, T.G.Chart, Calphad, 14, 115-23(1990).  
_assessment that models this phase_

## TETRAGONAL_A6 (Ga–In)

- Id: `phase:ga-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 297.85–429.75 K, x(In) 0.96007–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-in:a6-tetragonal)

Names (5): _corpus: _corpus:phase:ga-in:a6-tetragonal  
_paper: _paper:10.1007/bf02663677:In  
_tdb: _tdb:GaIn-78Ans.tdb:TETRAGONAL_A6, tdb:GaIn-90Rug-LB.tdb:TETRAGONAL_A6, tdb:GaIn-91And.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (3): PHASE and CONSTITUENT statements as written

[GaIn-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-78Ans.tdb): TETRAGONAL_A6, type code %, sha256 `a710b6be14e94849…`

~~~~text
44: PHASE TETRAGONAL_A6 % 1 1 !
45: CONST TETRAGONAL_A6 : GA IN% : !
~~~~

[GaIn-90Rug-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-90Rug-LB.tdb): TETRAGONAL_A6, type code %, sha256 `8873223ef7171edc…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : GA IN% : !
~~~~

[GaIn-91And.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-91And.tdb): TETRAGONAL_A6, type code %, sha256 `4015efc6acf86024…`

~~~~text
45: PHASE TETRAGONAL_A6 % 1 1 !
46: CONST TETRAGONAL_A6 : GA IN% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02663677](https://doi.org/10.1007/BF02663677) T.J. Anderson, I. Ansara, J. Phase Equilib., 12, 64-72(1991).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90013-P](https://doi.org/10.1016/0364-5916%2890%2990013-P) B.C. Rugg, T.G.Chart, Calphad, 14, 115-23(1990).  
_assessment that models this phase_

## BCC_A2 (Ga–In)

- Id: `phase:ga-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-in:bcc-a2)

Names (4): _corpus: _corpus:phase:ga-in:bcc-a2  
_tdb: _tdb:GaIn-78Ans.tdb:BCC_A2, tdb:GaIn-90Rug-LB.tdb:BCC_A2, tdb:GaIn-91And.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[GaIn-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-78Ans.tdb): BCC_A2, type code %B, sha256 `a710b6be14e94849…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : GA IN : VA : !
~~~~

[GaIn-90Rug-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-90Rug-LB.tdb): BCC_A2, type code %B, sha256 `8873223ef7171edc…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GA IN : VA : !
~~~~

[GaIn-91And.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-91And.tdb): BCC_A2, type code %B, sha256 `4015efc6acf86024…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : GA IN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02663677](https://doi.org/10.1007/BF02663677) T.J. Anderson, I. Ansara, J. Phase Equilib., 12, 64-72(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90013-P](https://doi.org/10.1016/0364-5916%2890%2990013-P) B.C. Rugg, T.G.Chart, Calphad, 14, 115-23(1990).  
_assessment that models this phase_

## FCC_A1 (Ga–In)

- Id: `phase:ga-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-in:fcc-a1)

Names (4): _corpus: _corpus:phase:ga-in:fcc-a1  
_tdb: _tdb:GaIn-78Ans.tdb:FCC_A1, tdb:GaIn-90Rug-LB.tdb:FCC_A1, tdb:GaIn-91And.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[GaIn-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-78Ans.tdb): FCC_A1, type code %A, sha256 `a710b6be14e94849…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : GA IN : VA : !
~~~~

[GaIn-90Rug-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-90Rug-LB.tdb): FCC_A1, type code %A, sha256 `8873223ef7171edc…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GA IN : VA : !
~~~~

[GaIn-91And.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-91And.tdb): FCC_A1, type code %A, sha256 `4015efc6acf86024…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : GA IN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02663677](https://doi.org/10.1007/BF02663677) T.J. Anderson, I. Ansara, J. Phase Equilib., 12, 64-72(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90013-P](https://doi.org/10.1016/0364-5916%2890%2990013-P) B.C. Rugg, T.G.Chart, Calphad, 14, 115-23(1990).  
_assessment that models this phase_

## HCP_A3 (Ga–In)

- Id: `phase:ga-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-in:hcp-a3)

Names (4): _corpus: _corpus:phase:ga-in:hcp-a3  
_tdb: _tdb:GaIn-78Ans.tdb:HCP_A3, tdb:GaIn-90Rug-LB.tdb:HCP_A3, tdb:GaIn-91And.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[GaIn-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-78Ans.tdb): HCP_A3, type code %A, sha256 `a710b6be14e94849…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : GA IN : VA: !
~~~~

[GaIn-90Rug-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-90Rug-LB.tdb): HCP_A3, type code %A, sha256 `8873223ef7171edc…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : GA IN : VA: !
~~~~

[GaIn-91And.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-91And.tdb): HCP_A3, type code %A, sha256 `4015efc6acf86024…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : GA IN : VA: !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02663677](https://doi.org/10.1007/BF02663677) T.J. Anderson, I. Ansara, J. Phase Equilib., 12, 64-72(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90013-P](https://doi.org/10.1016/0364-5916%2890%2990013-P) B.C. Rugg, T.G.Chart, Calphad, 14, 115-23(1990).  
_assessment that models this phase_

## LIQUID (Ga–In)

- Id: `phase:ga-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 297.85–2500 K, x(In) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-in:liquid)

Names (4): _corpus: _corpus:phase:ga-in:liquid  
_tdb: _tdb:GaIn-78Ans.tdb:LIQUID, tdb:GaIn-90Rug-LB.tdb:LIQUID, tdb:GaIn-91And.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[GaIn-78Ans.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-78Ans.tdb): LIQUID, type code %, sha256 `a710b6be14e94849…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : GA IN : !
~~~~

[GaIn-90Rug-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-90Rug-LB.tdb): LIQUID, type code %, sha256 `8873223ef7171edc…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GA IN : !
~~~~

[GaIn-91And.tdb](https://orchid-project.org/data/databases/sgte-binary/GaIn-91And.tdb): LIQUID, type code %, sha256 `4015efc6acf86024…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : GA IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02663677](https://doi.org/10.1007/BF02663677) T.J. Anderson, I. Ansara, J. Phase Equilib., 12, 64-72(1991).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(78)90008-1](https://doi.org/10.1016/0364-5916%2878%2990008-1) I. Ansara, J.P. Bros, C. Girard, Calphad, 2, 187-96(1978).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(90)90013-P](https://doi.org/10.1016/0364-5916%2890%2990013-P) B.C. Rugg, T.G.Chart, Calphad, 14, 115-23(1990).  
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
