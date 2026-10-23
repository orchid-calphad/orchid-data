# In–Si phases

> In–Si system: 3 phases (tier A 2, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-SI.html · Markdown: https://data.orchid-project.org/phases/pages/IN-SI.md

3 phases (tier A 2, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-SI) · [full JSON](https://data.orchid-project.org/phases/systems/IN-SI.json) · [In–Si system page](https://data.orchid-project.org/systems/IN-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Si system (3)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-in-si-a4-diamond); _phase:in-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1687 K, x(Si) 1–1 | 0 | 1 |
| [TETRAGONAL_A6](#phase-in-si-a6-tetragonal); _phase:in-si:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Si) 0–0 | 0 | 1 |
| [LIQUID](#phase-in-si-liquid); _phase:in-si:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(Si) 0–1 | 14 | 1 |

## DIAMOND_A4 (In–Si)

- Id: `phase:in-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1687 K, x(Si) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-si:a4-diamond)

Names (2): _corpus: _corpus:phase:in-si:a4-diamond  
_tdb: _tdb:InSi-85Ole-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[InSi-85Ole-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSi-85Ole-LB.tdb): DIAMOND_A4, type code %, sha256 `f6a4df494b9b3444…`

~~~~text
26: PHASE DIAMOND_A4 % 1 1 !
27: CONST DIAMOND_A4 : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02869223](https://doi.org/10.1007/BF02869223) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diagrams, 6, 128-30(1985).  
_assessment that models this phase_

## TETRAGONAL_A6 (In–Si)

- Id: `phase:in-si:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Si) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-si:a6-tetragonal)

Names (2): _corpus: _corpus:phase:in-si:a6-tetragonal  
_tdb: _tdb:InSi-85Ole-LB.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InSi-85Ole-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSi-85Ole-LB.tdb): TETRAGONAL_A6, type code %, sha256 `f6a4df494b9b3444…`

~~~~text
31: PHASE TETRAGONAL_A6 % 1 1 !
32: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02869223](https://doi.org/10.1007/BF02869223) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diagrams, 6, 128-30(1985).  
_assessment that models this phase_

## LIQUID (In–Si)

- Id: `phase:in-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–2500 K, x(Si) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-si:liquid)

Names (3): _corpus: _corpus:phase:in-si:liquid  
_paper: _paper:10.1007/bf02869223:L  
_tdb: _tdb:InSi-85Ole-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InSi-85Ole-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InSi-85Ole-LB.tdb): LIQUID, type code %, sha256 `f6a4df494b9b3444…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : IN SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02869223](https://doi.org/10.1007/BF02869223) R.W. Olesinski, N. Kanani, G.J. Abbaschian, Bull. Alloy Phase Diagrams, 6, 128-30(1985).  
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
