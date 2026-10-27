# Ga–Hg phases

> Ga–Hg system: 3 phases (tier A 2, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-HG.html · Markdown: https://data.orchid-project.org/phases/pages/GA-HG.md

3 phases (tier A 2, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-HG) · [full JSON](https://data.orchid-project.org/phases/systems/GA-HG.json) · [Ga–Hg system page](https://data.orchid-project.org/systems/GA-HG.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-HG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Hg system (3)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBO_A10](#phase-ga-hg-a10-rhombo); _phase:ga-hg:a10-rhombo_ | alpha-Hg · A10 · hR1 · R-3m (166) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 3 | 2 |
| [ORTHORHOMBIC_A11](#phase-ga-hg-a11-orthorhombic); _phase:ga-hg:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 299.44–302.91 K, x(Hg) 0–0 | 3 | 2 |
| [LIQUID](#phase-ga-hg-liquid); _phase:ga-hg:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 299.44–2500 K, x(Hg) 0–1 | 3 | 2 |

## RHOMBO_A10 (Ga–Hg)

- Id: `phase:ga-hg:a10-rhombo`; status `assigned`
- Structure: alpha-Hg · A10 · hR1 · R-3m (166); type `st:a10-alpha-hg-hr1`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 3 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-hg:a10-rhombo)

Names (5): _corpus: _corpus:phase:ga-hg:a10-rhombo, corpus:phase:ga-hg:rhombo-a10  
_paper: _paper:10.1007/s11771-009-0005-7:(Hg)  
_tdb: _tdb:GaHg-09Fen.tdb:RHOMBO_A10, tdb:GaHg-91Ans-LB.tdb:RHOMBO_A10  


### TDB models of RHOMBO_A10 (2): PHASE and CONSTITUENT statements as written

[GaHg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaHg-09Fen.tdb): RHOMBO_A10, type code %, sha256 `d689d1f31debfa2a…`

~~~~text
26: PHASE RHOMBO_A10 % 1 1 !
27: CONST RHOMBO_A10 : HG : !
~~~~

[GaHg-91Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaHg-91Ans-LB.tdb): RHOMBO_A10, type code %, sha256 `b02caa627e3f0d5a…`

~~~~text
27: PHASE RHOMBO_A10 % 1 1 !
28: CONST RHOMBO_A10 : HG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## ORTHORHOMBIC_A11 (Ga–Hg)

- Id: `phase:ga-hg:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 299.44–302.91 K, x(Hg) 0–0
- Literature: 3 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-hg:a11-orthorhombic)

Names (5): _corpus: _corpus:phase:ga-hg:a11-orthorhombic, corpus:phase:ga-hg:orthorhombic-a11  
_paper: _paper:10.1007/s11771-009-0005-7:(Ga)  
_tdb: _tdb:GaHg-09Fen.tdb:ORTHORHOMBIC_A11, tdb:GaHg-91Ans-LB.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (2): PHASE and CONSTITUENT statements as written

[GaHg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaHg-09Fen.tdb): ORTHORHOMBIC_A11, type code %, sha256 `d689d1f31debfa2a…`

~~~~text
31: PHASE ORTHORHOMBIC_A11 % 1 1 !
32: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaHg-91Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaHg-91Ans-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `b02caa627e3f0d5a…`

~~~~text
32: PHASE ORTHORHOMBIC_A11 % 1 1 !
33: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ga–Hg)

- Id: `phase:ga-hg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 299.44–2500 K, x(Hg) 0–1
- Literature: 3 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-hg:liquid)

Names (4): _corpus: _corpus:phase:ga-hg:liquid  
_paper: _paper:10.1007/s11771-009-0005-7:L2  
_tdb: _tdb:GaHg-09Fen.tdb:LIQUID, tdb:GaHg-91Ans-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GaHg-09Fen.tdb](https://orchid-project.org/data/databases/sgte-binary/GaHg-09Fen.tdb): LIQUID, type code %, sha256 `d689d1f31debfa2a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GA HG : !
~~~~

[GaHg-91Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaHg-91Ans-LB.tdb): LIQUID, type code %, sha256 `b02caa627e3f0d5a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : GA HG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11771-009-0005-7](https://doi.org/10.1007/s11771-009-0005-7) Yan Feng, Ri-chu Wang, Chao-qun Peng, Hua-shan Liu, Thermodynamic reassessment of Ga-Hg and Mg-Hg systems, J. Cent. South Univ. Technol. 16, 32-37 (2009).  
_assessment that models this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
