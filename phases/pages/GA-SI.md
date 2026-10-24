# Ga–Si phases

> Ga–Si system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-SI.html · Markdown: https://data.orchid-project.org/phases/pages/GA-SI.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-SI) · [full JSON](https://data.orchid-project.org/phases/systems/GA-SI.json) · [Ga–Si system page](https://data.orchid-project.org/systems/GA-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Si system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-si-a11-orthorhombic); _phase:ga-si:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.41 K, x(Si) 0–0 | 0 | 2 |
| [DIAMOND_A4](#phase-ga-si-a4-diamond); _phase:ga-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Si) 0.99923–1 | 0 | 2 |
| [BCC_A2](#phase-ga-si-bcc-a2); _phase:ga-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ga-si-fcc-a1); _phase:ga-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ga-si-hcp-a3); _phase:ga-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ga-si-liquid); _phase:ga-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 302.91–2500 K, x(Si) 0–1 | 11 | 2 |

## ORTHORHOMBIC_A11 (Ga–Si)

- Id: `phase:ga-si:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.41 K, x(Si) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-si:a11-orthorhombic)

Names (3): _corpus: _corpus:phase:ga-si:a11-orthorhombic  
_tdb: _tdb:GaSi-05Fra-LB.tdb:ORTHORHOMBIC_A11, tdb:GaSi-85Ole.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (2): PHASE and CONSTITUENT statements as written

[GaSi-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-05Fra-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `90a1f15279062a1c…`

~~~~text
45: PHASE ORTHORHOMBIC_A11 % 1 1 !
46: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaSi-85Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-85Ole.tdb): ORTHORHOMBIC_A11, type code %, sha256 `fab542640f16379f…`

~~~~text
45: PHASE ORTHORHOMBIC_A11 % 1 1 !
46: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02880523](https://doi.org/10.1007/BF02880523) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 362-64(1095).  
_assessment that models this phase_

## DIAMOND_A4 (Ga–Si)

- Id: `phase:ga-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Si) 0.99923–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-si:a4-diamond)

Names (3): _corpus: _corpus:phase:ga-si:a4-diamond  
_tdb: _tdb:GaSi-05Fra-LB.tdb:DIAMOND_A4, tdb:GaSi-85Ole.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[GaSi-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-05Fra-LB.tdb): DIAMOND_A4, type code %, sha256 `90a1f15279062a1c…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : GA SI% : !
~~~~

[GaSi-85Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-85Ole.tdb): DIAMOND_A4, type code %, sha256 `fab542640f16379f…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02880523](https://doi.org/10.1007/BF02880523) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 362-64(1095).  
_assessment that models this phase_

## BCC_A2 (Ga–Si)

- Id: `phase:ga-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-si:bcc-a2)

Names (3): _corpus: _corpus:phase:ga-si:bcc-a2  
_tdb: _tdb:GaSi-05Fra-LB.tdb:BCC_A2, tdb:GaSi-85Ole.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GaSi-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-05Fra-LB.tdb): BCC_A2, type code %B, sha256 `90a1f15279062a1c…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GA SI : VA : !
~~~~

[GaSi-85Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-85Ole.tdb): BCC_A2, type code %B, sha256 `fab542640f16379f…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GA SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02880523](https://doi.org/10.1007/BF02880523) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 362-64(1095).  
_assessment that models this phase_

## FCC_A1 (Ga–Si)

- Id: `phase:ga-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-si:fcc-a1)

Names (3): _corpus: _corpus:phase:ga-si:fcc-a1  
_tdb: _tdb:GaSi-05Fra-LB.tdb:FCC_A1, tdb:GaSi-85Ole.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GaSi-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-05Fra-LB.tdb): FCC_A1, type code %A, sha256 `90a1f15279062a1c…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GA SI : VA : !
~~~~

[GaSi-85Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-85Ole.tdb): FCC_A1, type code %A, sha256 `fab542640f16379f…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GA SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02880523](https://doi.org/10.1007/BF02880523) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 362-64(1095).  
_assessment that models this phase_

## HCP_A3 (Ga–Si)

- Id: `phase:ga-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-si:hcp-a3)

Names (3): _corpus: _corpus:phase:ga-si:hcp-a3  
_tdb: _tdb:GaSi-05Fra-LB.tdb:HCP_A3, tdb:GaSi-85Ole.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GaSi-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-05Fra-LB.tdb): HCP_A3, type code %A, sha256 `90a1f15279062a1c…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : GA SI : VA : !
~~~~

[GaSi-85Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-85Ole.tdb): HCP_A3, type code %A, sha256 `fab542640f16379f…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : GA SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02880523](https://doi.org/10.1007/BF02880523) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 362-64(1095).  
_assessment that models this phase_

## LIQUID (Ga–Si)

- Id: `phase:ga-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 302.91–2500 K, x(Si) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-si:liquid)

Names (4): _corpus: _corpus:phase:ga-si:liquid  
_paper: _paper:10.1007/bf02880523:L  
_tdb: _tdb:GaSi-05Fra-LB.tdb:LIQUID, tdb:GaSi-85Ole.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GaSi-05Fra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-05Fra-LB.tdb): LIQUID, type code %, sha256 `90a1f15279062a1c…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GA SI : !
~~~~

[GaSi-85Ole.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSi-85Ole.tdb): LIQUID, type code %, sha256 `fab542640f16379f…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GA SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02880523](https://doi.org/10.1007/BF02880523) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 362-64(1095).  
_assessment that models this phase; reports values for this phase_

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
